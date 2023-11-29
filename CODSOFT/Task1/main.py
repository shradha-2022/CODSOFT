import random

# Define responses for greetings
GREETING_RESPONSES = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define responses for different types of questions
QUESTION_RESPONSES = {
    "who are you?": "I am a rule-based chatbot.",
    "what can you do?": "I can respond to greetings, basic questions, and provide information.",
    "how are you?": "I'm just a computer program, so I don't have feelings, but thanks for asking!",
    "what is your purpose?": "My purpose is to assist and provide information to users.",
    "where are you from?": "I exist in the realm of computer programs and algorithms!",
    "what is the meaning of life?": "The meaning of life is a philosophical question that differs from person to person.",
    "default": "I'm sorry, I don't have an answer to that question right now."
}

# Function to handle greetings
def handle_greeting():
    return random.choice(GREETING_RESPONSES)

# Function to handle different types of questions
def handle_question(user_input):
    user_input = user_input.lower()
    response = QUESTION_RESPONSES.get(user_input, QUESTION_RESPONSES["default"])
    return response

# Function to generate bot response
def get_bot_response(user_input):
    if user_input.lower() in ["hello", "hi", "hey", "greetings"]:
        return handle_greeting()
    else:
        return handle_question(user_input)

# Chat loop
def start_chat():
    print("Bot: Hi! I am a rule-based chatbot. You can start chatting or type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        bot_response = get_bot_response(user_input)
        print("Bot:", bot_response)

# Start the chat
if __name__ == "__main__":
    start_chat()