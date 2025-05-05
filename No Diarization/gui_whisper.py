import streamlit as st
import whisper
import tempfile
import os
import srt
import json
import csv
from datetime import timedelta
import shutil
from langcodes import Language
import pprint

# Titolo dell'app
st.set_page_config(page_title="Whisper GUI", layout="centered")
st.title("🎙️ Trascrizione Audio con Whisper")

# Selezione del modello
model_size = st.selectbox("Seleziona il modello Whisper", ["tiny", "base", "small", "medium", "large"], index=1)

# Avviso sui modelli piccoli
if model_size in ["tiny", "base"]:
    st.warning("⚠️ I modelli 'tiny' e 'base' potrebbero non rilevare correttamente la lingua. Usa almeno 'small' per risultati più affidabili.")

# Selezione modalità
task_mode = st.radio("Modalità", ["Trascrivi nella lingua originale", "Traduci in inglese (⚠️ Whisper traduce solo verso l'inglese)"])

st.markdown("""
<div style='color:gray; font-size:0.9em;'>
🔎 <strong>Nota:</strong> Se selezioni la modalità "Traduci in inglese", Whisper effettuerà automaticamente la traduzione del parlato nella lingua rilevata <u>verso l'inglese</u>. 
Al momento non è possibile tradurre in altre lingue.
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Carica un file audio", type=["mp3", "wav", "m4a"])

@st.cache_resource
def load_model(model_size):
    return whisper.load_model(model_size)

model = load_model(model_size)
tmp_path = None

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if st.button("Trascrivi audio"):
        with st.spinner('Trascrizione in corso...'):
            whisper_task = "translate" if task_mode.startswith("Traduci") else "transcribe"

            result = model.transcribe(
                tmp_path,
                task=whisper_task,
                verbose=True,
                word_timestamps=False
            )

            transcription = result["text"]
            language = result.get("language", None)
            segments = result.get("segments", [])

            st.success("Trascrizione completata!")

            # Lingua rilevata
            if language:
                try:
                    language_name = Language.get(language).display_name("it")
                except:
                    language_name = language
                st.markdown(f"**Lingua rilevata:** `{language_name}` (`{language}`)")
            else:
                st.warning("❗ Lingua non rilevata automaticamente.")
                language_name = st.selectbox("Seleziona la lingua dell'audio:", [
                    "italiano", "inglese", "spagnolo", "francese", "tedesco", "portoghese", "russo", "arabo", "urdu", "cinese", "giapponese"
                ])
                language = Language.find(language_name).language

            if task_mode.startswith("Traduci") and language != "en":
                st.info(f"Traduzione automatica da **{language_name}** verso **inglese** completata con successo ✨")

            st.text_area("Testo trascritto:", transcription, height=300)

            # DEBUG opzionale
            if st.checkbox("Mostra output completo di Whisper (debug)"):
                st.code(json.dumps(result, indent=2, ensure_ascii=False), language="json")

            # Generazione file SRT
            def to_srt(segments):
                entries = []
                for i, seg in enumerate(segments):
                    start = timedelta(seconds=int(seg['start']))
                    end = timedelta(seconds=int(seg['end']))
                    content = seg['text'].strip()
                    entries.append(srt.Subtitle(index=i+1, start=start, end=end, content=content))
                return srt.compose(entries)

            srt_data = to_srt(segments)
            vtt_data = srt_data.replace(" --> ", ".")
            json_data = json.dumps(segments, indent=2, ensure_ascii=False)
            csv_data = "start,end,text\n" + "\n".join(
                f"{s['start']},{s['end']},\"{s['text'].replace('\"', '\"')}\"" for s in segments
            )

            base_filename = os.path.splitext(uploaded_file.name)[0]

            st.download_button("Scarica .txt", transcription, file_name=f"{base_filename}.txt", mime="text/plain")
            st.download_button("Scarica .srt", srt_data, file_name=f"{base_filename}.srt", mime="application/x-subrip")
            st.download_button("Scarica .vtt", vtt_data, file_name=f"{base_filename}.vtt", mime="text/vtt")
            st.download_button("Scarica .json", json_data, file_name=f"{base_filename}.json", mime="application/json")
            st.download_button("Scarica .csv", csv_data, file_name=f"{base_filename}.csv", mime="text/csv")

            output_dir = "trascrizioni_salvate"
            os.makedirs(output_dir, exist_ok=True)
            with open(os.path.join(output_dir, f"{base_filename}.txt"), "w", encoding="utf-8") as f:
                f.write(transcription)
            with open(os.path.join(output_dir, f"{base_filename}.srt"), "w", encoding="utf-8") as f:
                f.write(srt_data)
            with open(os.path.join(output_dir, f"{base_filename}.vtt"), "w", encoding="utf-8") as f:
                f.write(vtt_data)
            with open(os.path.join(output_dir, f"{base_filename}.json"), "w", encoding="utf-8") as f:
                f.write(json_data)
            with open(os.path.join(output_dir, f"{base_filename}.csv"), "w", encoding="utf-8") as f:
                f.write(csv_data)

            st.info(f"Trascrizioni salvate anche in: `{output_dir}/`")

# --- Cronologia file salvati ---
st.subheader("📁 Cronologia file trascritti")
output_dir = "trascrizioni_salvate"
if os.path.exists(output_dir):
    files = sorted(os.listdir(output_dir))
    grouped = {}
    for f in files:
        base = os.path.splitext(f)[0]
        grouped.setdefault(base, []).append(f)

    for base_name, related_files in grouped.items():
        with st.expander(base_name):
            for f in related_files:
                file_path = os.path.join(output_dir, f)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                st.markdown(f"**{f}**")
                st.code(content[:1000] + ("..." if len(content) > 1000 else ""), language="text")
                with open(file_path, "rb") as fbin:
                    st.download_button(
                        label=f"⬇️ Scarica {f}",
                        data=fbin,
                        file_name=f,
                        mime="text/plain"
                    )
else:
    st.info("Nessun file trascritto trovato.")

# Cleanup file temporaneo
@st.cache_data
def cleanup():
    if tmp_path and os.path.exists(tmp_path):
        os.remove(tmp_path)
cleanup()
