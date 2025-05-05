
# 🎧 Whisper Speaker Diarization (Light Edition)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Light-green)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Questa è la versione leggera dell'app Streamlit per trascrizione + diarizzazione con:

- [Whisper](https://github.com/openai/whisper) per la trascrizione
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) per la diarizzazione dei parlanti

✅ Ottimizzato per funzionare su sistemi con risorse limitate (senza GPU)
✅ Nessun uso di SpeechBrain

---

## ✨ Funzionalità

- Trascrizione automatica o traduzione verso inglese
- Diarizzazione leggera dei parlanti (Speaker 0, 1, 2...)
- Interfaccia Web semplice via Streamlit
- ✅ Esportazione in:
  - `.txt` (trascrizione completa)
  - `.srt` (sottotitoli con speaker)
  - `.json` (segmenti e metadati)

---

## 📦 Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
huggingface-cli login  # solo al primo utilizzo
streamlit run whisper_diarization_standalone.py
```

---

## 🔐 Requisiti

- Python ≥ 3.8
- `ffmpeg` installato nel sistema
- Token Hugging Face con permessi "read"
- Accettazione termini:
  - [pyannote/speaker-diarization](https://huggingface.co/pyannote/speaker-diarization)
  - [pyannote/segmentation](https://huggingface.co/pyannote/segmentation)

---

## 📁 File inclusi

- `whisper_diarization_standalone.py` – script principale
- `requirements.txt` – librerie necessarie

---

## 🧾 Licenza

Licenza MIT. Basato su software open source: OpenAI Whisper, Pyannote, Streamlit.
