from simple_chatbot import ChatBot

def test_chat():
    bot = ChatBot(api_key="sk-...", model="gpt-4")
    reply = bot.chat("Who won the World Cup in 2022?")
    assert isinstance(reply, str)
