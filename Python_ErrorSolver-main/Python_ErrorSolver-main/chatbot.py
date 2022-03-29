# Importing everything needed
import random
from data_base import search_process

# Naming bot
bot_name = 'sara:'

response = {'hi', 'hello', 'hola', 'hey'}

# Chat starts here
def chatting(get_response):
    
    if get_response in response:
        return 'Hello...  Type your Error below'
    
    elif 'end' in get_response:
        return "terminate"

    elif 'exit' in get_response:
        return "terminate"
    
    else:
        return search_process(get_response)
        
