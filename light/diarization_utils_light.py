
from pyannote.audio import Pipeline

def load_diarization_pipeline(hf_token: str):
    try:
        pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=hf_token)
        return pipeline
    except Exception as e:
        print("❌ Errore nel caricamento della diarization pipeline:", e)
        return None

def assign_speakers_to_whisper_segments(whisper_segments, diarization_result):
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
