
# ✍️ Whisper Transcription (No Diarization)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Transcription-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Interfaccia minimal per trascrivere e tradurre file audio usando OpenAI Whisper.

---

## ✅ Funzionalità

- Trascrizione nella lingua originale
- Traduzione automatica verso inglese
- Download di `.txt`, `.srt`, `.json`, `.csv`

---

## 🚀 Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_whisper_transcribe_only.py
```

---

## 📁 File

- `streamlit_whisper_transcribe_only.py`
- `requirements.txt`

---

## 🔖 Requisiti

- Python 3.8+
- ffmpeg installato
- Non richiede token Hugging Face
