import google.generativeai as genai
import PIL.Image

# 1. Apni purani API key yahan paste karo
genai.configure(api_key="AIzaSyD3d1adZaRBd-HsjjczBXFUU6ThZQ4G0_E")

def get_ai_report(image_path):
    try:
        # Gemini 1.5 Flash use kar rahe hain (kafi fast hai)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Photo load karo
        img = PIL.Image.open(image_path)
        
        # AI ko instruction do
        prompt = "Explain who is this person and what is he doing in this security footage? Be concise."
        
        # AI se response lo
        response = model.generate_content([prompt, img])
        return response.text
    except Exception as e:
        return f"AI Reporting Error: {e}"