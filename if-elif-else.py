while True:
    user_input: str = input('You:')
    if user_input == 'hello':
        print('Bot: Hello!')

    elif user_input == 'how are you ?':
        print('Bot: Good, how about you?')
    
    elif user_input == 'I am fine':
        print('Bot: Wow great!')

    elif user_input == 'bye':
        print('Bot: Goodbye!')

    else:
        print('Bot: Sorry, I did not understand that.')

