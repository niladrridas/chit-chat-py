from chitchatpy import ChitChatBot

# Create a ChitChatBot instance
chatbot = ChitChatBot()

# Define a function for more complex interactions
def interact_with_chatbot(user_input):
    # Get a response from the chatbot
    response = chatbot.get_response(user_input)
    
    # Perform additional processing based on the response
    if "suggest a movie" in user_input.lower():
        response = "Sure! How about watching 'Inception' for a mind-bending experience or 'The Shawshank Redemption' for a powerful drama?"
    elif "buying a sports car" in user_input.lower():
        response = "Great choice! Consider checking out models like the Ferrari 488, Lamborghini Huracan, or Porsche 911 for an exhilarating driving experience."
    elif "tell me more about" in user_input.lower():
        # You can extend this logic to provide more information based on user queries
        response = "I'd be happy to tell you more about that! What specific details are you interested in?"

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
