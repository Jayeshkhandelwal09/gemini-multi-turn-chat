# Gemini Multi-Turn Chat

A simple interactive console-based chatbot using the Google Gemini API. This chatbot maintains conversation context across multiple turns and allows customization of model parameters.

## Features

- Interactive console-based chat interface
- Maintains conversation context across multiple turns
- Customizable model parameters (temperature and top-p)
- Simple to use and extend

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your Google Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root
   - Add your API key: `GOOGLE_API_KEY=your_api_key_here`

## Usage

Run the chatbot:
```bash
python gemini_chat.py
```

The script will:
1. Prompt you for model parameters (temperature and top-p)
   - Press Enter to use defaults
   - Temperature controls response creativity (0.0-1.0)
   - Top-p controls response focus (0.0-1.0)
2. Start an interactive chat session
3. Type your messages and get responses from Gemini
4. Type 'quit' to exit the chat

## Example Conversation

```
Model Parameters (press Enter for defaults):
Temperature (0.0-1.0, default=0.7):
Top-p (0.0-1.0, default=0.8):

Chat started! (Type 'quit' to exit)

You: What is artificial intelligence?
Gemini: [Gemini's response about AI]

You: Can you give me a specific example?
Gemini: [Gemini's contextualized response with examples]

You: quit
```

## Notes

- The chatbot uses the 'gemini-1.0-pro' model
- Conversation history is maintained throughout the session
- API key is loaded securely from the .env file
- Error handling is implemented for API issues