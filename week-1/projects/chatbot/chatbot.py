from ai_client import client, handle_client_error, ai_client

class Chatbot:


    def __init__(self):
        self.chat_history = []
    
    def clear_history(self):
        self.chat_history = []

    def process_input (self, prompt):

        if prompt.lower() == "quit":
            return "quit"
        elif prompt.lower() == "clear":
            return "clear"
        elif prompt.lower() == "help":
            return "help"
        else:
            user_message = {"role": "user", "parts": [{"text": prompt}]}
            self.chat_history.append(user_message)

            response = ai_client(self.chat_history)
            model_message =  {"role": "model", "parts": [{"text": response.text}]}
            self.chat_history.append(model_message)

            return response.text


if __name__ == "__main__":
    bot = Chatbot()
    print("Welcome to your chatbot script!")
    print("Type your question to ask something, \"clear\" to clean the chat history, and \"quit\" to exit")

    while True:
        try:
            prompt = input("What's your question?").strip()
            result = bot.process_input(prompt)

            if result == "quit":
                print("Bye!")
                break

            elif result == "clear":
                bot.clear_history()
                print("Chat history erased!")

            elif result == "help":
                print("use \"quit\" to exit the chat")
                print("use \"clear\" to clear chat history")

            else:
                print(result)
                print("\n")

        except Exception as e:
            if handle_client_error(e) == "quota exceeded":
                break
            else:
                print("something went wrong!")
                print(e)


