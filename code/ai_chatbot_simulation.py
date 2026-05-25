# AI Chatbot Simulation

import random

print("🤖 AI Chatbot Activated")

responses = [
    "Hello! How can I help you?",
    "Welcome to the virtual world!",
    "AI systems are running successfully.",
    "Have a great day!"
]

user_message = input("👤 You: ")

reply = random.choice(responses)

print("🤖 Chatbot:", reply)
