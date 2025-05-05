
# 🎙️ Whisper Speaker Diarization (Light Edition)

Questo progetto è una GUI web costruita con [Streamlit](https://streamlit.io/) che utilizza [Whisper](https://github.com/openai/whisper) per la trascrizione automatica di file audio e [pyannote-audio](https://github.com/pyannote/pyannote-audio) per la diarizzazione dei parlanti.

È progettata per essere **leggera** e compatibile anche con ambienti a risorse limitate (senza GPU), evitando modelli pesanti come quelli di `speechbrain`.

---

## 🚀 Funzionalità principali

- Caricamento di file audio (`.mp3`, `.wav`, `.m4a`)
- Trascrizione automatica nella lingua originale o traduzione in inglese
- Riconoscimento dei parlanti (Speaker 0, Speaker 1, ...)
- Interfaccia web semplice via Streamlit
- Basato esclusivamente su `Whisper` e `pyannote.audio` (niente `speechbrain`)
- Ottimizzato per macchine con meno di 8GB di RAM

---

## 📦 Requisiti

- Python 3.8+
- ffmpeg installato nel sistema
- Ambiente virtuale consigliato

---

## 🔧 Setup

### 1. Clona la repo o scarica lo zip
```bash
git clone https://github.com/tuo-utente/whisper-diarization-light.git
cd whisper-diarization-light
```

### 2. Crea e attiva un ambiente virtuale
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

> 🧠 Importante: `whisper` viene installato direttamente dal repository GitHub ufficiale di OpenAI.

---

## 🔐 Token Hugging Face

Questo progetto richiede l'uso dei modelli `pyannote/speaker-diarization`.  
Per accedervi, devi:

1. Creare un account su [https://huggingface.co](https://huggingface.co)
2. Generare un token da: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Accettare i termini del modello:
   - [pyannote/speaker-diarization](https://huggingface.co/pyannote/speaker-diarization)
   - [pyannote/segmentation](https://huggingface.co/pyannote/segmentation)
4. Eseguire il login una volta sola:
```bash
huggingface-cli login
```

---

## ▶️ Avvio

Esegui l'app con:
```bash
streamlit run whisper_diarization_standalone.py
```

---

## 📤 Output

- Trascrizione testuale con speaker
- Visualizzazione diretta nella UI
- (Prossimamente) download di file `.srt`, `.txt`, `.json`

---

## 📁 File principali

- `whisper_diarization_standalone.py`: script principale
- `requirements.txt`: dipendenze del progetto
- `diarization_utils_light.py`: funzioni ausiliarie per pyannote (se usate separatamente)

---

## 📃 Licenza

Questo progetto è distribuito con licenza **MIT**.  
Assicurati di rispettare le licenze dei modelli utilizzati (OpenAI, Hugging Face, PyTorch, ecc.).

---

## 🙌 Crediti

- [OpenAI Whisper](https://github.com/openai/whisper)
- [pyannote-audio](https://github.com/pyannote/pyannote-audio)
- [Streamlit](https://streamlit.io/)
