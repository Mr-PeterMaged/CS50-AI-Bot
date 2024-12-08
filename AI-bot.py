import google.generativeai as genai
import json
from datetime import datetime

# Configure the GenAI API
api_key = "AIzaSyD86ZOy4b2_Qt4bg_6OUIx5XqK-Y9rTQkQ"
genai.configure(api_key=api_key)

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Start the chat with an empty history
chat = model.start_chat(history=[])

# Chat history storage file
chat_history_file = "chat-history.json"

print("Welcome to the chatbot! Type 'exit' to end the conversation.")

# Load existing chat history if the file exists
try:
    with open(chat_history_file, "r") as file:
        chat_history = json.load(file)
except FileNotFoundError:
    chat_history = []

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Send the user's message to the model
    response = chat.send_message(user_input)

    # Store the interaction with timestamp
    chat_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user_input,
        "bot": response.text
    }
    chat_history.append(chat_entry)

    # Save the updated chat history to the file in real-time
    with open(chat_history_file, "w") as file:
        json.dump(chat_history, file, indent=4)

    # Print the model's response
    print(f"Bot: {response.text}")
