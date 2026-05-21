# Day 1 Exercises - AI Overview & Setup

## 🎯 Learning Goals
- Set up development environment
- Understand AI terminology
- Make first API interaction
- Document learning process

## 📝 Exercise 1: Environment Setup (15 minutes)

### Task: Complete Development Setup
1. **Verify Python installation**
   ```bash
   python --version  # Should be 3.8+
   ```

2. **Create virtual environment**
   ```bash
   python -m venv ai-env
   source ai-env/bin/activate  # macOS/Linux
   # ai-env\Scripts\activate  # Windows
   ```

3. **Install required packages**
   ```bash
   cd week-1
   pip install -r requirements.txt
   ```

4. **Test installation**
   ```bash
   python -c "import openai; print('OpenAI package ready!')"
   ```

### ✅ Success Criteria:
- [X] Virtual environment created and activated
- [X] All packages installed without errors
- [X] Python can import openai package

## 🤖 Exercise 2: AI Terminology Quiz (5 minutes)

### Task: Match Terms to Definitions
Connect each term with its correct definition:

**Terms:**
1. Artificial Intelligence (AI) - B
2. Machine Learning (ML) - A
3. Large Language Model (LLM) - D
4. API - C
5. Token - E

**Definitions:**
A. A subset of AI that learns patterns from data
B. The broad field of making machines intelligent
C. A way for programs to communicate with services
D. An AI model trained on text to understand and generate language
E. Units that AI models use to process text

### Answer Key:
1-B, 2-A, 3-D, 4-C, 5-E

## 💬 Exercise 3: Prompt Exploration (10 minutes)

### Task: Test Different Prompting Styles
Use ChatGPT or Claude to try these different approaches:

1. **Basic prompt**: "What is Python programming?"

2. **Specific prompt**: "Explain Python programming in 3 sentences for someone who knows basic computer skills but hasn't coded before."

3. **Role-based prompt**: "You are a helpful coding teacher. Explain what Python is and why it's good for beginners."

4. **Format-specific prompt**: "List 5 reasons why Python is popular, with each reason in one sentence."

### Observation Notes:
Record what you notice:
- Which prompts gave the most helpful responses?
- How did the AI's tone change with different approaches?
- What was surprising about the responses?

### ✅ Success Criteria:
- [X] Tested all 4 prompt styles
- [X ] Noted differences in responses
- [X ] Identified which style worked best for you

---

## 🏆 Bonus Challenges (if you have extra time)

### Bonus 1: Create Your API Account
1. Go to https://platform.openai.com
2. Create an account
3. Navigate to API keys section
4. Generate your first API key (keep it secret!)
5. Copy the env template and add your key

### Bonus 2: Explore AI Tools
Visit these AI tools and try them briefly:
- ChatGPT (chat.openai.com)
- Claude (claude.ai)  
- GitHub Copilot (if you have access)
- Replit AI (replit.com)

Document what each tool seems best at.

### Bonus 3: Read About AI Applications
Find one article or video about AI being used in:
- Healthcare
- Education  
- Creative industries
- Software development

Write 2-3 sentences about what you learned.

---

## 📝 Reflection Questions

After completing the exercises, answer these questions in your daily log:

1. **What was the most interesting thing you learned about AI today?**

2. **What part of the setup was most challenging?**

3. **Which prompting style felt most natural to you?**

4. **What are you most excited to learn next?**

5. **What questions do you have about AI development?**

## 🎯 Tomorrow's Preparation

Before tomorrow's session:
- [X ] Ensure your API key is working (if you got one)
- [ ] Review the `api-quickstart.md` guide
- [ ] Think of a simple project idea for your first chatbot

**Tomorrow's Focus**: Making your first programmatic API call and exploring AI applications!

---

*Remember: The goal is exploration and learning, not perfection. If something doesn't work exactly right, that's normal and valuable learning experience!*