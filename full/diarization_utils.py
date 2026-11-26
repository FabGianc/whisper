
from pyannote.audio import Pipeline
from speechbrain.pretrained import SpeakerRecognition
from typing import List, Dict
import torchaudio

def load_diarization_pipeline(hf_token: str):
    try:
        pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=hf_token)
        return pipeline
    except Exception as e:
        print("❌ Errore nel caricamento della diarization pipeline:", e)
        return None

def assign_speakers_to_whisper_segments(whisper_segments: List[Dict], diarization_result) -> List[Dict]:
    speaker_segments = []

    for ws in whisper_segments:
        start = ws['start']
        end = ws['end']
        matched_speakers = []

        for turn, _, speaker in diarization_result.itertracks(yield_label=True):
            if turn.end > start and turn.start < end:
                matched_speakers.append(speaker)

        speaker_assigned = matched_speakers[0] if matched_speakers else "Speaker ?"
        speaker_segments.append({
            "start": start,
            "end": end,
            "text": ws['text'],
            "speaker": speaker_assigned
        })

    return speaker_segments

def identify_speaker(audio_path: str, speaker_segments: List[Dict]) -> List[Dict]:
    # Optional: assegnazione speaker con SpeechBrain
    try:
        recognizer = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb")
    except Exception as e:
        print("Errore nel caricamento SpeechBrain:", e)
        return speaker_segments

    signal, fs = torchaudio.load(audio_path)
    embeddings = []

    for segment in speaker_segments:
        start_sample = int(segment['start'] * fs)
        end_sample = int(segment['end'] * fs)
        audio_chunk = signal[:, start_sample:end_sample]

        if audio_chunk.shape[1] > 1000:
            try:
                emb = recognizer.encode_batch(audio_chunk)
                embeddings.append((segment, emb))
            except:
                continue

    # Placeholder: ritorna speaker_segments senza identificazione
    return speaker_segments
