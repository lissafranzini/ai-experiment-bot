from ai_client import client, handle_client_error, ai_client

chat_history = []

while True:
    try:
        question = input("What's your question?").strip()

        if question.lower() == "quit":
            print ("Bye!")
            break

        elif question == "clear":
            chat_history = []
            print ("Chat history erased!")

        else:

            user_message = {"role": "user", "parts": [{"text": question}]}
            chat_history.append(user_message)

            response = ai_client(chat_history)

            model_message =  {"role": "model", "parts": [{"text": response.text}]}
                   
            
            print (response.text)
            print("\n")
            chat_history.append(model_message)

    except Exception as e:
        if handle_client_error(e) == "quota exceeded":
            break
        else:
            print ("something went wrong!")
            print (e)


