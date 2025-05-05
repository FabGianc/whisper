
# 🎙️ Whisper + Speaker Diarization (Versione Completa)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Diarization-brightgreen)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Questa versione dell'app utilizza **OpenAI Whisper** per la trascrizione automatica e **pyannote.audio** per la diarizzazione dei parlanti, integrando anche **SpeechBrain** per il riconoscimento vocale avanzato.

È pensata per sistemi **con almeno 8–12 GB di RAM**, preferibilmente con GPU.

---

## 🚀 Funzionalità principali

- Trascrizione automatica nella lingua originale o traduzione in inglese
- Diarizzazione: rileva chi sta parlando e segmenta le voci
- Identificazione vocale: assegna speaker univoci ai turni di parola
- Interfaccia Streamlit interattiva e user-friendly
- Esportazione prevista in `.txt`, `.json`, `.srt`, `.csv`, ecc.

---

## 📦 Setup

### 1. Crea e attiva un ambiente virtuale
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Installa i requisiti
```bash
pip install -r requirements.txt
```

---

## 🔐 Token Hugging Face

1. Vai su https://huggingface.co/settings/tokens
2. Crea un access token (permessi: read)
3. Esegui:
```bash
huggingface-cli login
```

4. Accetta i termini di questi modelli:
   - [pyannote/speaker-diarization](https://huggingface.co/pyannote/speaker-diarization)
   - [pyannote/segmentation](https://huggingface.co/pyannote/segmentation)

---

## ▶️ Avvio

```bash
streamlit run streamlit_whisper_diarization.py
```

---

## 📁 File inclusi

- `streamlit_whisper_diarization.py`: interfaccia principale
- `diarization_utils.py`: funzioni ausiliarie per pyannote + speechbrain
- `requirements_full.txt`: pacchetti Python richiesti

---

## ⚠️ Requisiti hardware consigliati

- CPU recente con almeno 4 core
- 8–16 GB di RAM
- Scheda GPU compatibile con PyTorch (opzionale ma consigliata)
- ffmpeg installato

---

## 📃 Licenza

Distribuito sotto licenza **MIT**.  
Rispettare le licenze di Whisper, pyannote.audio, SpeechBrain e altri tool open source utilizzati.
