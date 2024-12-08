# Chatbot with Google Generative AI

#### Video Demo:  [Insert Video URL Here]

---

## Description

This project is a simple yet interactive chatbot powered by Google's Generative AI (Gemini-1.5-Flash model). The chatbot allows users to have a natural language conversation, with all interactions stored in a JSON file for reference or further analysis. It is designed to demonstrate the capabilities of Google's Generative AI API in creating conversational applications.

The project can serve as a foundational base for more advanced AI-driven chatbots, such as those designed for customer support, virtual assistants, or educational tools. With a modular design, it is straightforward to expand its functionality or integrate it with other systems.

---

## Files

### `chatbot.py`
This is the main Python script that runs the chatbot application. It includes:
- **API Configuration:** Uses an API key to configure the Generative AI SDK.
- **Model Initialization:** Loads the Gemini-1.5-Flash model for generating responses.
- **Chat History Management:** Reads and writes chat history to a `chat-history.json` file, ensuring persistence across sessions.
- **Conversation Loop:** Maintains an ongoing dialogue with the user until the `exit` command is given.

### `chat-history.json`
This file stores the chat history in JSON format. Each entry contains:
- Timestamp of the interaction.
- User's input message.
- Bot's generated response.

This file ensures that all conversations are saved for future review or analysis.

---

## Features

- **Natural Language Interaction:** Engage in free-flowing conversations with the chatbot.
- **Persistent Chat History:** Saves every interaction, including timestamps, for easy reference.
- **Real-Time Response:** Responses are generated dynamically using Google's cutting-edge AI model.
- **Simple and Intuitive Interface:** Users interact with the chatbot via the terminal, making it accessible for testing and educational purposes.

---

## Design Choices

### Generative Model
The Gemini-1.5-Flash model was chosen for its efficiency and ability to generate coherent and context-aware responses. This ensures that the chatbot provides meaningful and relevant answers to user inputs.

### Persistent Storage
JSON was selected for storing chat history due to its simplicity, readability, and compatibility with Python's built-in libraries. This choice makes it easy to manipulate and analyze stored data for future enhancements or reporting.

### Modular Design
The script is designed to be modular and extensible, allowing for:
- Integration with other APIs or models.
- Additional features, such as sentiment analysis or multi-turn context handling.
- Deployment in web or mobile applications with minor modifications.

---

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install Dependencies:** Ensure you have Python 3.8+ installed and install the required library:
   ```bash
   pip install google-generativeai
   ```
3. **Set Up API Key:** Replace the placeholder in the code with your Google Generative AI API key:
   ```python
   api_key = "YOUR_API_KEY"
   ```
4. **Run the Chatbot:**
   ```bash
   python chatbot.py
   ```

---

## Future Improvements

- **Enhanced UI:** Add a graphical user interface for a more user-friendly experience.
- **Contextual Memory:** Improve the chatbot's ability to remember previous conversation context within a session.
- **Deployment:** Host the chatbot as a web service using frameworks like Flask or FastAPI.
- **Advanced Analytics:** Integrate analytics to evaluate the chatbot's performance and user engagement.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

