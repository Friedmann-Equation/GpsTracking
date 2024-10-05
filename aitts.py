import assemblyai as aai
from elevenlabs import generate, stream
from openai import OpenAI

class AI_Assistant:
    def __init__(self):
        aai.settings.api_key = "API-KEY"
        self.openai_client = OpenAI(api_key = "API-KEY")
        self.elevenlabs_api_key = "API-KEY"
        
        self.transcriber = None
        
        self.full_transcript = [
            {"role":"system", "content":"You are a personal assistant for someone who is either visually impaired or has alzheimer's disease."},
        ]
        
        