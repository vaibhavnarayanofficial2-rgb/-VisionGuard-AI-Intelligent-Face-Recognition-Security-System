import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def get_ai_report(log_data):
    if not GEMINI_KEY:
        return "Security Alert: Someone detected!"

    try:
        # Configuration setup
        genai.configure(api_key=GEMINI_KEY)
        
        # Sabse stable model call karne ka tareeka
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        response = model.generate_content(f"Summarize this alert in 5 words: {log_data}")
        return response.text
    except Exception as e:
        # Agar AI fail ho jaye, to project crash na ho, bas ye text bhej de
        print(f"⚠️ AI Logging Error: {e}")
        return "Alert: Suspicious activity detected near camera!"