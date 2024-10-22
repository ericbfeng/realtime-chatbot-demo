import os
from dotenv import load_dotenv
from elevenlabs import play, stream
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

# Get API key from environment
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

ELEVENLABS_VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # Default voice, you can change this


client = ElevenLabs(
  api_key= ELEVENLABS_API_KEY # Defaults to ELEVEN_API_KEY
)

#https://github.com/elevenlabs/elevenlabs-python?tab=readme-ov-file#input-streaming

def speak_stream(text, generate_response_stream):
    try:
        audio = client.generate(
                text=generate_response_stream(text),
                voice=ELEVENLABS_VOICE_ID,
                model="eleven_monolingual_v1",
                stream = True
        )
        stream(audio)
    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}")