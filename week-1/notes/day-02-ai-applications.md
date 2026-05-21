# Day 2: AI Applications Exploration

## 🎯 Today's Objectives
- Survey popular AI tools and their capabilities
- Explore different AI APIs and services
- Make your first programmatic AI API call
- Understand the AI ecosystem

## 🌍 AI Landscape Overview

### Major AI Categories

#### 1. **Text Generation & Understanding**
- **GPT-4/ChatGPT**: Conversational AI, writing assistance
- **Claude**: Anthropic's conversational AI with strong reasoning
- **Gemini**: Google's multimodal AI system
- **Use Cases**: Writing, coding, analysis, tutoring

#### 2. **Code Generation**
- **GitHub Copilot**: AI pair programmer
- **CodeT5/CodeGen**: Open-source code models
- **Cursor**: AI-powered code editor
- **Use Cases**: Auto-completion, bug fixing, code explanation

#### 3. **Image Generation**
- **DALL-E 3**: OpenAI's image generator
- **Midjourney**: Artistic image creation
- **Stable Diffusion**: Open-source image generation
- **Use Cases**: Art, design, prototyping, marketing

#### 4. **Specialized Tools**
- **Whisper**: Speech-to-text transcription
- **ElevenLabs**: Text-to-speech synthesis
- **RunwayML**: Video editing and generation
- **Use Cases**: Content creation, accessibility, automation

## 🔌 API Exploration

### OpenAI API Capabilities
- **Chat Completions**: Conversational interactions
- **Function Calling**: Structured tool usage
- **Vision**: Image understanding and analysis
- **Audio**: Speech and music processing

### Anthropic Claude API
- **Messages API**: Conversational interactions
- **Long Context**: Handle very long documents
- **Constitutional AI**: Helpful, harmless, honest responses

### Hugging Face Hub
- **Open Models**: Free access to thousands of models
- **Inference API**: Easy model deployment
- **Transformers Library**: Local model usage

## 💻 First API Call

### Setup Your Environment
```python
# first_api_call.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your API key
load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# Make your first API call
def test_api():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you explain what you are in one sentence?"}
            ],
            max_tokens=100
        )
        
        print("AI Response:")
        print(response.choices[0].message.content)
        
        print(f"\\nTokens used: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
```

## 🎯 Today's Experiments

### Experiment 1: Compare AI Models
Ask the same question to different AI services:
- ChatGPT (OpenAI)
- Claude (Anthropic) 
- Gemini (Google)

**Test Question**: "Explain quantum computing in simple terms"

### Experiment 2: Different Use Cases
Try AI for different tasks:
1. **Creative Writing**: "Write a short story about a robot learning to paint"
2. **Code Help**: "Explain this Python code: `list(zip(*matrix))`"
3. **Analysis**: "What are the pros and cons of remote work?"
4. **Learning**: "Teach me the basics of HTTP requests"

### Experiment 3: API Parameters
Test how parameters affect responses:
```python
# High creativity (temperature=1.0)
# Low creativity (temperature=0.1) 
# Different max_tokens values
```

## 📊 Understanding Costs & Limits

### Token Economics
- **Input tokens**: What you send to the AI
- **Output tokens**: What the AI generates
- **Context window**: Maximum total tokens per conversation

### Pricing Overview (check latest prices)
- **GPT-3.5-turbo**: ~$0.001 per 1K input tokens
- **GPT-4**: ~$0.03 per 1K input tokens
- **Claude**: Competitive pricing with longer context

### Rate Limits
- **Free tier**: Usually 3 requests per minute
- **Paid tier**: Much higher limits
- **Best practice**: Add delays between requests

## 🔍 Market Research Activity

### Explore These Tools (5 minutes each)
1. **Chat Interfaces**: ChatGPT, Claude, Perplexity
2. **Code Tools**: GitHub Copilot, CodeWhisperer, Codeium  
3. **Creative Tools**: DALL-E, Midjourney (Discord), Canva AI
4. **Productivity**: Notion AI, Grammarly, Jasper

### Document Your Findings
For each tool, note:
- What it's designed for
- How easy it is to use
- What impressed you most
- Potential use cases for your projects

## 📝 Daily Reflection

### Key Questions to Answer:
1. **Which AI tool surprised you the most today?**
2. **What types of tasks seem best suited for AI assistance?**
3. **What concerns or limitations did you notice?**
4. **Which API would you most like to explore further?**

### Technical Notes:
- Did your first API call work?
- What error messages did you encounter?
- How long did the API response take?

## 🔗 Resources

### Essential Documentation:
- [OpenAI API Guide](https://platform.openai.com/docs/guides)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Hugging Face API](https://huggingface.co/docs/api-inference/)

### Comparison Resources:
- [AI Model Comparison Chart](https://artificialanalysis.ai/)
- [LLM Leaderboards](https://chat.lmsys.org/?leaderboard)

## ⏭️ Tomorrow Preview: Day 3
- Dive deeper into AI limitations and ethics
- Learn about hallucinations and bias
- Practice better prompting techniques
- Start planning your chatbot project

---

**Today's Success**: If you made one successful API call and explored at least 3 different AI tools, you've accomplished the goal! 🎉