
import streamlit as st
import whisper
import tempfile
import os
import json
import srt
import shutil
from datetime import timedelta
from langcodes import Language
from pydub import AudioSegment
from huggingface_hub import get_token

from diarization_utils import load_diarization_pipeline, assign_speakers_to_whisper_segments

HF_TOKEN = get_token()

st.set_page_config(page_title="Whisper + Diarizzazione Completa", layout="centered")
st.title("🎙️ Trascrizione + Diarizzazione (completa)")

model_size = st.selectbox("Modello Whisper", ["tiny", "base", "small", "medium", "large"], index=2)
if model_size in ["tiny", "base"]:
    st.warning("⚠️ I modelli 'tiny' e 'base' potrebbero non rilevare correttamente la lingua.")

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
        with st.spinner("Trascrizione in corso..."):
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

        with st.spinner("Diarizzazione in corso..."):
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
            st.markdown("### 🎧 Risultato con speaker")

            for s in annotated:
                start = str(timedelta(seconds=int(s['start'])))
                st.markdown(f"🗣️ **{s['speaker']}** [{start}]: {s['text'].strip()}")
