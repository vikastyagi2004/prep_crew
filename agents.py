import os
from dotenv import load_dotenv
from groq import Groq
 
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-20b"
 
 
class Agent:
    def __init__(self, name, role):
        self.name = name    # a label, for printing
        self.role = role    # the system prompt: its job and rules
 
    def speak(self, message):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.role},
                {"role": "user", "content": message},
            ],
            temperature=0.3,
            reasoning_effort="low",
            max_completion_tokens=1500,
        )
        return response.choices[0].message.content.strip()
