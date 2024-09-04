import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def transcribe_audio(file_path):
    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(file.name, file.read()),
            model="distil-whisper-large-v3-en",
        )
    return transcription.text

if __name__ == "__main__":
    audio_file_path = "record_out.m4a"
    transcribed_text = transcribe_audio(audio_file_path)
    print(transcribed_text)
