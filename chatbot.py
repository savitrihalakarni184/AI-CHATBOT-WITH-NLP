# chatbot.py

from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you today?"]),
    (r"how are you?", ["I'm doing well, thank you!", "All systems are running smoothly."]),
    (r"what is your name?", ["I'm NLTKBot, your Python-powered assistant."]),
    (r"who created you?", ["I was created by SAVITRI S H using Python and NLTK."]),
    (r"what can you do?", ["I can answer simple questions, keep you company, and help with Python tasks."]),
    (r"tell me a joke", ["Why did the Python programmer go broke? Because he couldn't C#!"]),
    (r"what is python?", ["Python is a high-level, interpreted programming language known for its readability."]),
    (r"what is NLP?", ["NLP stands for Natural Language Processing. It helps machines understand human language."]),
    (r"thank you", ["You're welcome!", "Glad I could help!", "Anytime!"]),
    (r"(.*) (weather|temperature) (.*)", ["I'm not connected to live weather data yet, but you can use OpenWeatherMap API for that."]),
    (r"(.*) (location|city)", ["I'm based in the cloud, accessible from anywhere."]),
    (r"(.*) help (.*)", ["I can assist with Python, NLP, and basic queries. Just ask!"]),
    (r"(.*) your favorite language?", ["Python, of course!"]),
    (r"(.*) (bye|goodbye)", ["Goodbye! Have a great day!", "See you later!"]),
    (r"quit", ["Exiting... Take care!"])
]

# Run the chatbot
def run_chatbot():
    print("Hi! I'm NLTKBot. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    run_chatbot()