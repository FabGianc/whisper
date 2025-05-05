
# ✍️ Whisper Transcription

---

## 🎙️No Diarization -> Whisper GUI – Trascrizione Audio con Interfaccia Streamlit

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Transcription-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Un'interfaccia web semplice e intuitiva per trascrivere e tradurre file audio utilizzando il modello [Whisper](https://github.com/openai/whisper) di OpenAI, realizzata con [Streamlit](https://streamlit.io/).

---

# 🎙️ Whisper + Speaker Diarization (Versione Completa)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Diarization-brightgreen)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Questa versione dell'app utilizza **OpenAI Whisper** per la trascrizione automatica e **pyannote.audio** per la diarizzazione dei parlanti, integrando anche **SpeechBrain** per il riconoscimento vocale avanzato.

È pensata per sistemi **con almeno 8–12 GB di RAM**, preferibilmente con GPU.

---

## 📁 File

- `streamlit_whisper_transcribe_only.py`
- `requirements.txt`

---

## 🔖 Requisiti

- Python 3.8+
- ffmpeg installato
- Non richiede token Hugging Face
