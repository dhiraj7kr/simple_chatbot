# simple_chatbot/chatbot.py
import openai

class ChatBot:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        self.history = [{"role": "system", "content": "You are a helpful assistant."}]
        openai.api_key = self.api_key

    def chat(self, message: str) -> str:
        self.history.append({"role": "user", "content": message})
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.history
            )
            reply = response['choices'][0]['message']['content']
            self.history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"Error: {str(e)}"
