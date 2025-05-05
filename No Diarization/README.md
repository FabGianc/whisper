# 🎙️ Whisper GUI – Trascrizione Audio con Interfaccia Streamlit

Un'interfaccia web semplice e intuitiva per trascrivere e tradurre file audio utilizzando il modello [Whisper](https://github.com/openai/whisper) di OpenAI, realizzata con [Streamlit](https://streamlit.io/).

---

## ✨ Funzionalità

- Caricamento file audio (`.mp3`, `.wav`, `.m4a`)
- Selezione del modello Whisper (`tiny` → `large`)
- Trascrizione nella lingua originale
- Traduzione automatica verso l'inglese
- Esportazione dei risultati in formato `.txt`, `.srt`, `.vtt`, `.json`, `.csv`
- Cronologia delle trascrizioni salvate localmente

---

## 🛠️ Installazione

### 1. Clona il repository
```bash
git clone https://github.com/tuo-utente/whisper-gui.git
cd whisper-gui
```

### 2. Crea un ambiente virtuale e attivalo

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Installa le dipendenze
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Avvio dell'app

Lancia l'interfaccia con Streamlit:

```bash
streamlit run gui_whisper.py
```

Apri il browser all’indirizzo mostrato da Streamlit (tipicamente `http://localhost:8501`).

---

## 📁 Output

Le trascrizioni verranno salvate nella cartella `trascrizioni_salvate/` nei formati:
- `.txt` – Testo semplice
- `.srt` – Sottotitoli
- `.vtt` – WebVTT
- `.json` – Output dettagliato con segmenti
- `.csv` – Segmenti con timestamp

---

## 🧠 Requisiti

- Python ≥ 3.8
- Connessione a Internet (per scaricare i modelli Whisper al primo utilizzo)
- Architettura compatibile con PyTorch (CPU o GPU)

---

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

---

## 🙌 Riconoscimenti

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Streamlit](https://streamlit.io/)
- [srt](https://github.com/cdown/srt)
- [langcodes](https://pypi.org/project/langcodes/)
