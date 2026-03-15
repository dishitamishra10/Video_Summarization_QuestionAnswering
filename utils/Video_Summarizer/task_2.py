from faster_whisper import WhisperModel

model = WhisperModel(
    "base.en",
    device='cpu',
    compute_type='int8'
)

def video_audio_text(video_file):
    segments, _ = model.transcribe(
        video_file,
        beam_size=3
    )

    all_transcript = "\n".join(segment.text for segment in segments)
    

    return all_transcript.strip()