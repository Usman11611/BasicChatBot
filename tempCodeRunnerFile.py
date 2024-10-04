import re  # Import the regular expression module for string operations
import textgenerator as tg  # Import a custom text generator module, presumably for predefined bot replies

def calculate_match_probability(user_input, target_words, is_single_response=False, required_keywords=[]):
    match_count = 0  # Initialize the count of matched words
    required_words_present = True  # Assume required keywords are present

    # Count how many target words are found in the user input
    for word in user_input:
        if word in target_words:
            match_count += 1  # Increment match count for each matching word

    # Calculate the percentage of recognized words in the user input
    match_percentage = float(match_count) / float(len(target_words))  # Calculate the ratio of matched words to target words

    # Check if all required keywords are present in the input
    for word in required_keywords:
        if word not in user_input:
            required_words_present = False  # Set flag to False if a required keyword is missing
            break  # Exit loop early if any required keyword is missing

    # Return the match percentage if conditions are met
    if required_words_present or is_single_response:
        return int(match_percentage * 100)  # Convert the match percentage to an integer (0-100 scale)
    else:
        return 0  # Return 0 if required keywords are missing and it's not a single response scenario

def evaluate_all_inputs(user_message):
    response_confidence = {}  # Initialize a dictionary to store the confidence scores of each response

    # Simplify response creation and add it to the dictionary
    def create_response(bot_reply, keywords, is_single_response=False, required_keywords=[]):
        nonlocal response_confidence  # Access the outer scope dictionary
        response_confidence[bot_reply] = calculate_match_probability(user_message, keywords, is_single_response, required_keywords)  # Store the match probability for the response

    # Predefined responses
    create_response('Hi there!', ['hello', 'hi', 'hey', 'what\'s up', 'heya'], is_single_response=True)  # Greet the user
    create_response('Goodbye!', ['bye', 'farewell', 'takecare'], is_single_response=True)  # Respond to farewells
    create_response('I\'m well, how about you?', ['how', 'are', 'you', 'doing'], required_keywords=['how'])  # Respond to inquiries about well-being
    create_response('No problem!', ['thank', 'thanks'], is_single_response=True)  # Respond to thanks
    create_response('Appreciate it!', ['i', 'love', 'coding', 'place'], required_keywords=['coding', 'place'])  # Respond to expressions of appreciation for a place related to coding

    # More complex responses
    create_response(tg.ADVICE_REPLY, ['need', 'advice'], required_keywords=['advice'])  # Provide advice when needed
    create_response(tg.FOOD_REPLY, ['what', 'do', 'you', 'eat'], required_keywords=['you', 'eat'])  # Respond to questions about food preferences

    best_response = max(response_confidence, key=response_confidence.get)  # Determine the response with the highest confidence score

    return tg.unknown_response() if response_confidence[best_response] < 1 else best_response  # Return the best response or an unknown response if confidence is too low

# Main function to generate the bot's response
def generate_bot_reply(user_input):
    split_input = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())  # Split the user input into words using regex
    reply = evaluate_all_inputs(split_input)  # Evaluate the input and get the best response
    return reply  # Return the generated reply

# Start the chatbot interaction
while True:
    print('Bot: ' + generate_bot_reply(input('You: ')))  # Continuously prompt the user for input and respond
