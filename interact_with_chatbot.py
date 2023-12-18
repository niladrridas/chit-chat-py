from chitchatpy import ChitChatBot

# Create a ChitChatBot instance
chatbot = ChitChatBot()

# Define a function for more complex interactions
def interact_with_chatbot(user_input):
    # Get a response from the chatbot
    response = chatbot.get_response(user_input)
    
    # Perform additional processing based on the response
    if "tell me a joke" in user_input.lower():
        response = "Why don't scientists trust atoms? Because they make up everything!"
    elif "calculate" in user_input.lower():
        try:
            # Attempt to perform a simple calculation
            calculation_result = eval(user_input.split("calculate")[1])
            response = f"The result is: {calculation_result}"
        except Exception as e:
            response = "Sorry, I couldn't perform the calculation. Please check your input."

    return response

# Main loop for interacting with the chatbot
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        break
    
    # Get a response using the extended interaction function
    response = interact_with_chatbot(user_input)
    
    print(f"ChitChatPy: {response}")
