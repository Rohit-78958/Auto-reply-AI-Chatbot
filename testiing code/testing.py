def is_last_response_from_sender(chat_history, sender="Mummi"):
    # Split the chat history into individual messages
    messages = chat_history.split("/2024]")
    print(messages)
    
    # Extract the last message (assuming it's the most recent)
    last_message = messages[-1]
    
    # Check if the last message contains "R B Ashwin"
    return sender in last_message



chat = '''

'''
print(is_last_response_from_sender(chat))