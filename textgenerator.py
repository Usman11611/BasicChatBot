import random  # Import the random module to allow selection of random elements from a list

# Predefined bot reply for questions about food
FOOD_REPLY = "As a robot, I don't have to eat, but thanks for asking!"

# Predefined bot reply for general advice requests
ADVICE_REPLY = "I'd suggest searching the web for exactly what you mentioned!"

# Function to provide a response when the bot doesn't understand the user's input
def unknown_response():
    reply_options = [  # List of possible replies when the bot doesn't recognize the input
        "Can you rephrase that?",  # Suggests the user try saying it differently
        "...",  # A neutral, non-committal response
        "I'm not sure I follow.",  # Indicates the bot didn't understand
        "What do you mean by that?"  # Asks the user for clarification
    ]
    return random.choice(reply_options)  # Return a randomly selected reply from the list