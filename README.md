
# 🗣️ Whisper Transcription

Una semplice interfaccia web per la trascrizione automatica di file audio basata su [Whisper](https://github.com/openai/whisper) di OpenAI, con elaborazione **locale** e interfaccia grafica realizzata in **Streamlit**.

## 🚀 Funzionalità

- Trascrizione di file audio in diverse lingue
- Identificazione automatica della lingua
- Traduzione in inglese (opzionale)
- Elaborazione **completamente offline**
- Interfaccia user-friendly basata su Streamlit

## 🛠️ Requisiti

- Python 3.8+
- Pytorch (con supporto CUDA consigliato per prestazioni migliori)
- `whisper` (OpenAI)
- `streamlit`
---

## 🎙️No Diarization -> Whisper GUI – Trascrizione Audio con Interfaccia Streamlit

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Transcription-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Un'interfaccia web semplice e intuitiva per trascrivere e tradurre file audio utilizzando il modello [Whisper](https://github.com/openai/whisper) di OpenAI, realizzata con [Streamlit](https://streamlit.io/).

---

## 🎙️ full -> Whisper + Speaker Diarization (Versione Completa)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Diarization-brightgreen)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Questa versione dell'app utilizza:

- [Whisper](https://github.com/openai/whisper) per la trascrizione automatica
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) per la diarizzazione dei parlanti
- integrando anche [SpeechBrain](https://github.com/speechbrain/speechbrain) per il riconoscimento vocale avanzato.

✅ È pensata per sistemi **con almeno 8–12 GB di RAM**, preferibilmente con GPU.

---

## 🎙️ light -> Whisper Speaker Diarization (Light Edition)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Whisper--Light-green)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

Questa è la versione leggera dell'app Streamlit per trascrizione + diarizzazione con:

- [Whisper](https://github.com/openai/whisper) per la trascrizione
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) per la diarizzazione dei parlanti

✅ Ottimizzato per funzionare su sistemi con risorse limitate (senza GPU)

✅ Nessun uso di SpeechBrain
