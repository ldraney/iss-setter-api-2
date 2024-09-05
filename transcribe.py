import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Check if the API key is set
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file")

client = Groq(api_key=api_key)

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    with open(file_path, "rb") as file:
        try:
            transcription = client.audio.transcriptions.create(
                file=(file.name, file.read()),
                model="distil-whisper-large-v3-en",
            )
        except Exception as e:
            print(f"Error during transcription: {e}")
            return None
    return transcription.text

if __name__ == "__main__":
    audio_file_path = "record_out.m4a"
    transcribed_text = transcribe_audio(audio_file_path)
    if transcribed_text:
        print(transcribed_text)
    else:
        print("Transcription failed")
