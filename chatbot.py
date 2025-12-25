import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["My name is AI Chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! How about you?"]
    ],
    [
        r"what can you do ?",
        ["I can answer your basic questions and chat with you."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day 😊"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

def chatbot():
    print("🤖 AI Chatbot is ready! Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
