# Development Environment Setup Guide

## 🛠️ Required Tools

### 1. Python Environment
- **Python 3.8+**: Check with `python --version`
- **pip**: Python package manager
- **Virtual environments**: Use `venv` or `conda`

```bash
# Create virtual environment
python -m venv ai-env

# Activate (macOS/Linux)
source ai-env/bin/activate

# Activate (Windows)
ai-env\Scripts\activate
```

### 2. Code Editor
- **Cursor** (recommended) - AI-powered coding
- **VS Code** - Popular alternative with extensions
- **PyCharm** - Full-featured IDE

**Recommended Extensions:**
- Python extension
- GitLens
- REST Client (for API testing)

### 3. Version Control
- **Git**: Version control system
- **GitHub Account**: For project hosting

```bash
# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 4. API Testing Tools
- **Postman** (GUI) - API testing interface
- **curl** (command line) - Built into most systems
- **httpx/requests** (Python) - For programmatic API calls

## 🔑 API Accounts Setup

### Essential Services

1. **OpenAI** (https://platform.openai.com)
   - Create account
   - Get API key from API section
   - Start with free tier ($18 credit)

2. **GitHub** (https://github.com)
   - Create account for version control
   - Enable 2FA for security
   - Create your first repository

### Optional Services (for exploration)

3. **Anthropic/Claude** (https://console.anthropic.com)
   - Alternative to OpenAI
   - Different capabilities to explore

4. **Hugging Face** (https://huggingface.co)
   - Open-source AI models
   - Free tier available

## 📦 Python Dependencies

Create `requirements.txt` files for each week:

### Week 1 (Basic AI)
```
openai==1.51.0
python-dotenv==1.0.1
requests==2.31.0
```

### Week 2 (Testing & Organization)
```
pytest==8.3.3
black==24.8.0
flake8==7.1.1
```

### Week 3 (Advanced AI)
```
anthropic==0.34.2
tiktoken==0.8.0
```

### Week 4 (Web Development)
```
flask==3.0.3
fastapi==0.115.4
uvicorn==0.32.0
sqlite3  # Built-in with Python
```

## 🔐 Security Setup

### API Key Management
1. **Never hardcode API keys** in your code
2. **Use environment variables** with `.env` files
3. **Add `.env` to `.gitignore`**

```bash
# Create .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env

# Add to .gitignore
echo ".env" >> .gitignore
```

### Example `.env` file:
```
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=your-anthropic-key-here
```

## ✅ Setup Verification

Run this checklist to verify your setup:

```bash
# 1. Check Python version
python --version  # Should be 3.8+

# 2. Check pip
pip --version

# 3. Check git
git --version

# 4. Create and activate virtual environment
python -m venv test-env
source test-env/bin/activate  # macOS/Linux
# test-env\Scripts\activate  # Windows

# 5. Install test package
pip install requests

# 6. Test installation
python -c "import requests; print('Setup successful!')"

# 7. Deactivate virtual environment
deactivate
```

## 🚨 Troubleshooting

### Common Issues

1. **Python not found**
   - macOS: Install via Homebrew `brew install python`
   - Windows: Download from python.org
   - Linux: `sudo apt install python3`

2. **Permission errors**
   - Use virtual environments
   - Never use `sudo pip install`

3. **Git authentication**
   - Set up SSH keys or personal access tokens
   - Follow GitHub's authentication guide

### Getting Help

- **Python**: https://docs.python.org/3/
- **Git**: https://git-scm.com/doc
- **OpenAI API**: https://platform.openai.com/docs
- **Stack Overflow**: For specific coding questions

## 🎯 Next Steps

1. Complete this setup checklist
2. Create your GitHub repository
3. Start with Week 1, Day 1 activities
4. Join the learning community (bookmark helpful resources)

Remember: The goal is progress, not perfection. Start with the basics and build up gradually!