import google.generativeai as genai
import os
from dotenv import load_dotenv

def initialize_gemini():
    """Initialize the Gemini API client."""
    load_dotenv() 
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("Please set GOOGLE_API_KEY in your .env file")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

def get_user_parameters():
    """Get model parameters from user."""
    print("\nModel Parameters (press Enter for defaults):")
    temp = input("Temperature (0.0-1.0, default=0.7): ").strip()
    temp = float(temp) if temp else 0.7
    
    top_p = input("Top-p (0.0-1.0, default=0.8): ").strip()
    top_p = float(top_p) if top_p else 0.8
    
    return {
        "temperature": max(0.0, min(1.0, temp)), 
        "top_p": max(0.0, min(1.0, top_p))       
    }

def main():
    print("Initializing Gemini chatbot...")
    model = initialize_gemini()
    
    params = get_user_parameters()
    
    chat = model.start_chat(history=[])
    print("\nChat started! (Type 'quit' to exit)")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            break
            
        try:
            response = chat.send_message(
                user_input,
                generation_config=params
            )
            print("\nGemini:", response.text)
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            break

if __name__ == "__main__":
    main() 