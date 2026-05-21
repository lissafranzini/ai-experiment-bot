# Getting Started - 30-Day AI Learning Journey

Welcome to your AI learning adventure! This guide will help you get everything set up and ready for your 30-day journey.

## 🚀 Quick Start (5 minutes)

### 1. Initial Setup
```bash
# Navigate to your learning directory
cd ai-learning-journey

# Run the setup script
python setup.py
```

### 2. Configure Your Environment
```bash
# Edit the .env file with your API keys
cp templates/env-template.txt .env
# Add your OpenAI API key to .env
```

### 3. Start Learning
```bash
# Activate Week 1 environment
source ai-week-1/bin/activate  # macOS/Linux
# ai-week-1\Scripts\activate   # Windows

# Begin with Day 1
open week-1/notes/day-01-setup.md
```

## 📋 Pre-requisites Checklist

- [ ] **Python 3.8+** installed (`python --version`)
- [ ] **Git** installed (`git --version`)
- [ ] **Code editor** (VS Code, Cursor, or PyCharm)
- [ ] **OpenAI account** created (https://platform.openai.com)
- [ ] **GitHub account** created (https://github.com)
- [ ] **30 minutes daily** committed to learning

## 🗂️ Learning Structure

### Week 1: AI Fundamentals (Days 1-7)
**Goal**: Understand AI and build your first chatbot
- AI overview and applications
- First API calls and interactions
- Build a working chatbot project

### Week 2: Software Engineering (Days 8-14)  
**Goal**: Professional development practices
- Code organization and structure
- Version control with Git
- Testing and debugging techniques

### Week 3: AI Development (Days 15-21)
**Goal**: Advanced AI application building
- API integration patterns
- Prompt engineering mastery
- Data processing for AI

### Week 4: Web Integration (Days 22-28)
**Goal**: Build web applications with AI
- Web development basics
- Database integration
- Production deployment

### Week 5: Advanced Topics (Days 29-30)
**Goal**: Performance and capstone project
- Optimization techniques
- Comprehensive project design

## 📚 Daily Routine

### Your 30-Minute Sessions
1. **5 minutes**: Review previous notes
2. **20 minutes**: Main learning activity
3. **5 minutes**: Update progress and plan tomorrow

### Documentation Habits
- Use `week-X/notes/` for daily learning notes
- Update `documentation/daily-log.md` with reflections
- Track progress in `documentation/progress-tracker.md`
- Commit code changes to Git regularly

## 🛠️ Tools You'll Use

### Development Environment
- **Python**: Primary programming language
- **Virtual Environments**: Isolated package management
- **Git/GitHub**: Version control and portfolio

### AI Services
- **OpenAI API**: GPT models for text generation
- **Anthropic Claude**: Alternative AI service
- **Hugging Face**: Open-source AI models

### Development Tools  
- **Code Editor**: VS Code, Cursor, or PyCharm
- **Terminal**: Command line interface
- **Postman**: API testing (optional)

## 🔧 Troubleshooting

### Common Setup Issues

1. **Python Version Errors**
   ```bash
   # Check version
   python --version
   
   # Use python3 if needed
   python3 --version
   ```

2. **Virtual Environment Issues**
   ```bash
   # Create new environment
   python -m venv ai-week-1
   
   # Activate (macOS/Linux)
   source ai-week-1/bin/activate
   
   # Activate (Windows)
   ai-week-1\Scripts\activate
   ```

3. **Package Installation Errors**
   ```bash
   # Upgrade pip first
   pip install --upgrade pip
   
   # Then install requirements
   pip install -r week-1/requirements.txt
   ```

4. **API Key Issues**
   ```bash
   # Check .env file exists
   ls -la .env
   
   # Verify API key format
   echo $OPENAI_API_KEY
   ```

### Getting Help
- **Documentation Issues**: Check the `resources/` directory
- **Code Problems**: Review examples in `templates/`
- **API Errors**: Consult `resources/api-quickstart.md`
- **Git Issues**: See GitHub documentation

## 📈 Success Metrics

### Weekly Goals
- **Week 1**: Working chatbot + API integration
- **Week 2**: Professional project structure + Git workflow
- **Week 3**: Advanced AI utility application
- **Week 4**: Web-based AI application with database
- **Week 5**: Capstone project design + optimization

### Daily Habits
- [ ] Complete 30-minute learning session
- [ ] Document learnings and challenges
- [ ] Practice coding and experimentation
- [ ] Commit progress to Git
- [ ] Reflect on the day's achievements

## 🎯 Learning Philosophy

### Growth Mindset
- **Progress over perfection**: Focus on learning, not perfect code
- **Experiment fearlessly**: Break things and learn from failures
- **Ask questions**: Document what confuses you
- **Build incrementally**: Start simple, add complexity gradually

### Practical Focus
- **Build real projects**: Every concept gets applied
- **Document your journey**: Create a portfolio you're proud of
- **Connect concepts**: See how everything fits together
- **Prepare for the future**: Build skills for continued learning

## 🎉 Ready to Begin?

1. **Complete the setup** using `python setup.py`
2. **Add your API keys** to the `.env` file
3. **Open** `week-1/notes/day-01-setup.md`
4. **Start your journey** with Day 1 activities

### Your First Command
```bash
# Activate Week 1 environment
source ai-week-1/bin/activate

# Start Day 1
cat week-1/notes/day-01-setup.md
```

**Welcome to your AI learning journey!** 🤖✨

In 30 days, you'll go from AI beginner to confident AI application developer. Let's get started!

---

*Questions or issues? Check the troubleshooting section above or review the documentation in the `resources/` directory.*