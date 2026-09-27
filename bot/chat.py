# Import Django configuration tools
import os
import django

# Configure Django settings so ChatterBot can use the Django database
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_project.settings")
django.setup()

# Import ChatterBot and its list-based trainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create the chatbot and use Django for database storage
chatbot = ChatBot(
    "AssignmentBot",
    storage_adapter="chatterbot.storage.DjangoStorageAdapter"
)

# Create a trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot using a sample conversation
trainer.train([
    "Good morning! How are you doing?",
    "I am doing very well, thank you for asking.",
    "You're welcome.",
    "Do you like hats?",
    "Yes, I like hats.",
    "That's great!"
])

# Start the terminal-based conversation
print("AssignmentBot is ready! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")

    # End the program when the user types "exit"
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Generate and display the chatbot's response
    response = chatbot.get_response(user_input)
    print("Bot:", response)