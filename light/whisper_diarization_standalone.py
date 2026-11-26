
import streamlit as st
import whisper
import tempfile
import os
import srt
import json
from datetime import timedelta
from langcodes import Language
from pydub import AudioSegment
from huggingface_hub import get_token

from diarization_utils_light import load_diarization_pipeline, assign_speakers_to_whisper_segments

HF_TOKEN = get_token()

st.set_page_config(page_title="Whisper + Diarizzazione Light", layout="centered")
st.title("🎙️ Trascrizione + Diarizzazione (Light)")

model_size = st.selectbox("Modello Whisper", ["tiny", "base", "small", "medium", "large"], index=2)
task_mode = st.radio("Modalità", ["Trascrivi nella lingua originale", "Traduci in inglese (⚠️ Whisper traduce solo verso l'inglese)"])
uploaded_file = st.file_uploader("Carica file audio", type=["mp3", "wav", "m4a"])

@st.cache_resource
def load_model(name):
    return whisper.load_model(name)

model = load_model(model_size)
tmp_path = None

if uploaded_file is not None:
    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    diar_wav_path = tmp_path + ".wav"
    sound = AudioSegment.from_file(tmp_path)
    sound.set_channels(1).set_frame_rate(16000).export(diar_wav_path, format="wav")

    if st.button("Trascrivi e assegna speaker"):
        with st.spinner("Trascrizione..."):
            whisper_task = "translate" if task_mode.startswith("Traduci") else "transcribe"
            result = model.transcribe(tmp_path, task=whisper_task)
            segments = result["segments"]
            transcription = result["text"]
            language = result.get("language", "non rilevata")

            try:
                lang_name = Language.get(language).display_name("it")
            except:
                lang_name = language
            st.markdown(f"**Lingua rilevata:** `{lang_name}` (`{language}`)")

        with st.spinner("Diarizzazione (pyannote)..."):
            diarization_pipeline = load_diarization_pipeline(HF_TOKEN)
            if diarization_pipeline is None:
                st.error("❌ Errore nella diarizzazione")
                st.stop()
            try:
                diar_result = diarization_pipeline(diar_wav_path)
            except Exception as e:
                st.error(f"❌ Diarizzazione fallita: {e}")
                st.stop()

            annotated = assign_speakers_to_whisper_segments(segments, diar_result)

            st.markdown("### 🎧 Trascrizione con speaker")
            srt_entries = []
            for i, s in enumerate(annotated):
                start = timedelta(seconds=int(s['start']))
                end = timedelta(seconds=int(s['end']))
                st.markdown(f"🗣️ **{s['speaker']}** [{start}]: {s['text'].strip()}")
                srt_entries.append(srt.Subtitle(index=i+1, start=start, end=end, content=f"{s['speaker']}: {s['text'].strip()}"))

            srt_data = srt.compose(srt_entries)
            json_data = json.dumps(annotated, indent=2, ensure_ascii=False)
            base_name = os.path.splitext(uploaded_file.name)[0]

            st.download_button("⬇️ Scarica .srt", srt_data, file_name=f"{base_name}_with_speaker.srt", mime="application/x-subrip")
            st.download_button("⬇️ Scarica .json", json_data, file_name=f"{base_name}_with_speaker.json", mime="application/json")
            st.download_button("⬇️ Scarica .txt", transcription, file_name=f"{base_name}.txt", mime="text/plain")
