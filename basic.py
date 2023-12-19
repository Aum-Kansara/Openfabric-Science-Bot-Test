# Use a pipeline as a high-level helper
from transformers import pipeline
from random import choice

pipe = pipeline("text-classification", model="dipesh/Intent-Classification-Bert-Base-Cased")
intents={'greet':["Hey! I appreciate the friendly hello. What's your question?","Hi there! Thanks for the greeting. Is there a particular query or question on your mind?","Hello! I'm at your service. Any specific questions or topics you'd like to explore about science?","Greetings! Your hello is welcomed. What's your question or inquiry for today?","Hey! I'm here for you. Do you have a query or something you'd like to discuss?","Hi! Thanks for reaching out. What can I help you with today? Any specific questions?","Hey! Your greeting is much appreciated. Do you have a question or something you'd like to know?"],
         'goodbye':["Goodbye! Feel free to return anytime.",
                    "Take care! See you soon.",
                    "Farewell! Reach out if needed.",
                    "So long! Have a great day.",
                    "Goodbye! Stay in touch.",
                    "Bye for now! Questions? Just ask.",
                    "See you later! Take care.",
                    "Adios! Need anything else?",
                    "Bye! Until we meet again."]}


result=pipe("abcjd")[0]
print(result)
if result['score']>0.5:
    detected_intent=result['label']
    if detected_intent in intents.keys():
        print("Response :",choice(intents[detected_intent]))
else:
    print('answer not found')