import whisper
import soundfile as sf
from gtts import gTTS

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

def synthesize_speech(text):
    tts = gTTS(text)
    output_path = "response.mp3"
    tts.save(output_path)
    return output_path
