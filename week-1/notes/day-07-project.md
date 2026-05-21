# Day 7: Week 1 Project - Build Your First Chatbot

## 🎯 Project Objectives
- Create a working chatbot using OpenAI API
- Implement conversation memory
- Add basic error handling
- Document your first AI project

## 🛠️ Project Requirements

### Core Features (Must Have)
- [ ] Connect to OpenAI API successfully
- [ ] Accept user input in a loop
- [ ] Send messages to AI and display responses
- [ ] Handle basic errors gracefully
- [ ] Allow user to exit the program

### Enhanced Features (Should Have)
- [ ] Maintain conversation history
- [ ] Clear conversation command
- [ ] Show conversation history command
- [ ] Basic input validation
- [ ] Friendly user interface

### Bonus Features (Nice to Have)
- [ ] Save conversations to file
- [ ] Load previous conversations
- [ ] Multiple conversation modes
- [ ] Token usage tracking
- [ ] Colorful console output

## 📁 Project Structure

Create this directory structure in `week-1/projects/`:
```
chatbot-project/
├── chatbot.py          # Main chatbot code
├── config.py          # Configuration settings
├── utils.py           # Helper functions
├── .env               # API keys (copy from template)
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── conversations/     # Saved conversations (optional)
```

## 🚀 Implementation Guide

### Step 1: Basic Chatbot Structure
Start with the template from `templates/basic-chatbot.py` and customize it.

### Step 2: Add Configuration
```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DEFAULT_MODEL = 'gpt-3.5-turbo'
    MAX_TOKENS = 150
    TEMPERATURE = 0.7
    
    # Validation
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
```

### Step 3: Add Helper Functions
```python
# utils.py
import json
from datetime import datetime

def save_conversation(conversation, filename=None):
    """Save conversation to JSON file."""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversations/chat_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(conversation, f, indent=2)
    
    print(f"Conversation saved to {filename}")

def load_conversation(filename):
    """Load conversation from JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []

def count_tokens_estimate(text):
    """Rough token count estimation (1 token ≈ 4 characters)."""
    return len(text) // 4
```

### Step 4: Enhanced Main Script
Extend the basic template with your new features:

```python
# chatbot.py
from config import Config
from utils import save_conversation, count_tokens_estimate
import os
from openai import OpenAI

class EnhancedChatbot:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.conversation_history = []
        self.total_tokens_used = 0
    
    # Add your enhanced methods here
    # (conversation management, file operations, etc.)
```

## 🧪 Testing Your Chatbot

### Test Cases to Try

1. **Basic Functionality**
   - Start the chatbot
   - Send a simple message
   - Get a response
   - Exit gracefully

2. **Conversation Memory**
   - Ask a question about your name
   - Tell the AI your name
   - Ask again - it should remember

3. **Commands**
   - Try 'clear' command
   - Try 'history' command
   - Try 'quit' command

4. **Error Handling**
   - Test with empty input
   - Test with very long input
   - Test without internet connection

### Expected Behavior
Your chatbot should:
- Respond appropriately to user messages
- Remember previous parts of the conversation
- Handle errors without crashing
- Provide clear commands and instructions

## 📝 Documentation Requirements

### README.md Template
```markdown
# My First AI Chatbot

## Description
A simple chatbot built with OpenAI's GPT-3.5 API that can have conversations and remember context.

## Features
- Interactive chat interface
- Conversation memory
- Basic commands (clear, history, quit)
- Error handling

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.template` to `.env` and add your OpenAI API key
3. Run: `python chatbot.py`

## Usage
- Type messages to chat with the AI
- Type 'clear' to reset conversation
- Type 'history' to see conversation log
- Type 'quit' to exit

## What I Learned
[Write about your experience building this]

## Challenges
[What was difficult and how you solved it]

## Next Steps
[Ideas for improvements]
```

## 🎯 Success Criteria

By the end of today, you should have:
- [ ] A working chatbot that can hold basic conversations
- [ ] Proper project structure with multiple files
- [ ] Basic error handling implemented
- [ ] Documentation written
- [ ] Code committed to version control

## 🔄 Iteration Process

### Version 1 (First 15 minutes)
- Get basic chatbot working
- Focus on making one successful conversation

### Version 2 (Next 10 minutes)
- Add conversation memory
- Improve user interface

### Version 3 (Last 5 minutes)
- Add commands and error handling
- Clean up code and add comments

## 🏆 Bonus Challenges

If you finish early:

1. **Personality**: Give your chatbot a specific personality or role
2. **Persistence**: Save and load conversations from files
3. **Statistics**: Track and display usage statistics
4. **Validation**: Add input validation and sanitization
5. **Styling**: Add colors or formatting to the console output

## 📚 Resources for Today

### Code References
- OpenAI Python SDK documentation
- Python file I/O tutorials
- JSON handling in Python
- Error handling best practices

### Debugging Tips
- Use print statements to see what's happening
- Check your .env file is properly configured
- Verify your API key is working with a simple test
- Start simple and add features gradually

## 🎉 Celebration

When you complete your chatbot:
1. Take a screenshot of it working
2. Write a brief reflection on what you learned
3. Commit your code to Git
4. Plan what you want to improve tomorrow

**Congratulations!** You've built your first AI application! 🤖✨

---

**Remember**: The goal is a working prototype, not perfection. Focus on getting something functional that you can improve over time.