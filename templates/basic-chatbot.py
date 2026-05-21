#!/usr/bin/env python3
"""
Basic AI Chatbot Template
Week 1 Project - Build your first AI application!

This template provides the structure for your chatbot.
Fill in the TODO sections as you learn.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

class BasicChatbot:
    def __init__(self):
        """Initialize the chatbot with OpenAI client."""
        # TODO: Set up the OpenAI client using your API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("Please set your OPENAI_API_KEY in the .env file")
        
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []
    
    def send_message(self, user_message):
        """
        Send a message to the AI and get a response.
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: The AI's response
        """
        try:
            # TODO: Add the user message to conversation history
            self.conversation_history.append({
                "role": "user", 
                "content": user_message
            })
            
            # TODO: Call the OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # Start with the cheaper model
                messages=self.conversation_history,
                max_tokens=150,  # Keep responses concise while learning
                temperature=0.7  # Balance creativity and consistency
            )
            
            # TODO: Extract the AI's response
            ai_message = response.choices[0].message.content
            
            # TODO: Add AI response to conversation history
            self.conversation_history.append({
                "role": "assistant", 
                "content": ai_message
            })
            
            return ai_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
        print("Conversation history cleared!")
    
    def show_history(self):
        """Display the conversation history."""
        if not self.conversation_history:
            print("No conversation history yet.")
            return
        
        print("\n--- Conversation History ---")
        for i, message in enumerate(self.conversation_history, 1):
            role = "You" if message["role"] == "user" else "AI"
            print(f"{i}. {role}: {message['content'][:100]}...")
    
    def run(self):
        """Start the interactive chatbot."""
        print("🤖 AI Chatbot Started!")
        print("Type 'quit' to exit, 'clear' to clear history, 'history' to show conversation")
        print("-" * 50)
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Handle special commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                elif user_input.lower() == 'history':
                    self.show_history()
                    continue
                elif not user_input:
                    print("Please enter a message.")
                    continue
                
                # Get AI response
                print("AI: ", end="", flush=True)
                response = self.send_message(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    """Main function to run the chatbot."""
    try:
        chatbot = BasicChatbot()
        chatbot.run()
    except ValueError as e:
        print(f"Setup Error: {e}")
        print("Please check your .env file and API key.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()