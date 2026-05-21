# Day 1: AI Overview & Environment Setup

## 🎯 Today's Objectives
- Understand what AI, Machine Learning, and Large Language Models are
- Set up your development environment
- Make your first AI interaction
- Plan your learning journey

## 📚 Learning Content

### What is AI?
**Artificial Intelligence (AI)** is technology that enables machines to perform tasks that typically require human intelligence.

### Key Concepts to Understand:

#### 1. **Artificial Intelligence (AI)**
- Broad field of making machines smart
- Includes everything from calculators to robots
- Goal: Simulate human-like thinking and problem-solving

#### 2. **Machine Learning (ML)**
- Subset of AI that learns from data (ML = using data to learn a function that maps inputs -> outputs. ex: spam labeling)
- Algorithms improve automatically through experience
- No need to program every possible scenario

#### 3. **Large Language Models (LLMs)**
- Type of ML specialized in understanding and generating text (LLMs il predict the next WORD)
- Trained on massive amounts of text data
- Examples: GPT-4, Claude, Gemini
- “Models learn the probability distribution of data and can sample from it.”

### Real-World AI Applications:
- **Text**: Writing assistance, translation, summarization
- **Images**: Photo editing, generation, recognition
- **Code**: Programming help, bug detection, code generation
- **Voice**: Speech recognition, text-to-speech
- **Decision Making**: Recommendations, analysis, predictions

## 🛠️ Setup Tasks

### 1. Environment Setup Checklist
- [X] Verify Python installation (`python --version`)
- [X] Create project directory
- [X] Set up virtual environment
- [X] Install basic packages

### 2. Account Creation
- [X] OpenAI Account (https://platform.openai.com)
- [X] GitHub Account (https://github.com)
- [X] Get OpenAI API key

### 3. First API Test

Create a simple test to verify your setup:

```python
# test_setup.py
import os
from openai import OpenAI

# Test 1: Check environment
print("Testing environment setup...")
print(f"Python working: {True}")

# Test 2: Check OpenAI (you'll add API key tomorrow)
print("OpenAI package installed: ", end="")
try:
    client = OpenAI()
    print("✓")
except ImportError:
    print("✗ - Need to install openai package")

print("Setup test complete!")
```

## 🔍 Exploration Activities

### ChatGPT Prompting Practice
Try these different prompting techniques with ChatGPT/Claude:

1. **Basic Question**: "What is machine learning?"

2. **Specific Request**: "Explain machine learning in simple terms for a beginner programmer"

3. **Role-based Prompt**: "You are a teacher. Explain machine learning to a student who knows basic Python"

4. **Step-by-step**: "List 5 steps to get started with AI development, with brief explanations"

### Observation Notes
Record what you notice about:
- How AI responds differently to different prompts
- What kinds of questions work best
- Any surprising or confusing responses

## 📝 Daily Reflection

### What I Learned Today:
- -c runs pythons command directly on the CLI, so I don't need to create a file to import libraries, for instance, I can do it on the CLI

### Questions I Have:
- [What are you still curious about?]

### Tomorrow's Goal:
- [What do you want to focus on tomorrow?]

## 🔗 Resources for Today

### Essential Reading:
- [OpenAI API Documentation](https://platform.openai.com/docs) - Skim the overview
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

### Optional Deep Dive:
- [What Is ChatGPT Doing?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) - Stephen Wolfram's explanation

### Tools Setup:
- Install VS Code or Cursor
- Configure Python extension
- Set up your first GitHub repository

## ⏭️ Tomorrow Preview: Day 2
- Dive deeper into AI applications
- Create your OpenAI API key
- Make your first programmatic AI API call
- Start building your first simple AI script

---

**Remember**: The goal today is orientation and setup. Don't worry about understanding everything - you'll build understanding gradually over 30 days!