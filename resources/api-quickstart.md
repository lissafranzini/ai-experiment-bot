# API Quick Start Guide

## 🚀 Making Your First API Call

### Step 1: Install Dependencies
```bash
pip install openai python-dotenv
```

### Step 2: Set Up Environment
1. Copy `templates/env-template.txt` to `.env`
2. Add your OpenAI API key to `.env`
3. Verify `.env` is in your `.gitignore`

### Step 3: Test Connection
```python
# test_api.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, AI!"}],
    max_tokens=50
)

print(response.choices[0].message.content)
```

## 📊 Understanding API Responses

### Response Structure
```python
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0613",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

### Key Components
- **choices[0].message.content**: The AI's response text
- **usage.total_tokens**: How many tokens were used (affects cost)
- **finish_reason**: Why the response ended ("stop", "length", etc.)

## ⚙️ Important Parameters

### Model Options
- **gpt-3.5-turbo**: Fast, cost-effective, good for learning
- **gpt-4**: More capable but more expensive
- **gpt-4-turbo**: Balance of capability and speed

### Key Parameters
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=150,        # Maximum response length
    temperature=0.7,       # Creativity (0.0-2.0)
    top_p=1.0,            # Alternative to temperature
    frequency_penalty=0.0, # Reduce repetition
    presence_penalty=0.0   # Encourage new topics
)
```

### Temperature Guide
- **0.0-0.3**: Focused, consistent, predictable
- **0.4-0.7**: Balanced creativity and consistency
- **0.8-1.0**: More creative and varied
- **1.1-2.0**: Highly creative, potentially inconsistent

## 🛡️ Error Handling

### Common Errors
```python
try:
    response = client.chat.completions.create(...)
    
except openai.RateLimitError:
    print("Rate limit exceeded. Wait a moment.")
    
except openai.AuthenticationError:
    print("Invalid API key.")
    
except openai.APIError as e:
    print(f"API error: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Rate Limits (Free Tier)
- **gpt-3.5-turbo**: 3 requests per minute
- **gpt-4**: 3 requests per minute
- Monitor usage at: https://platform.openai.com/usage

## 💰 Cost Management

### Token Counting
```python
import tiktoken

def count_tokens(text, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Example
prompt = "Hello, how are you?"
tokens = count_tokens(prompt)
print(f"Tokens: {tokens}")
```

### Pricing (approximate, check latest at openai.com)
- **gpt-3.5-turbo**: $0.001/1K input tokens, $0.002/1K output tokens
- **gpt-4**: $0.03/1K input tokens, $0.06/1K output tokens

### Cost Saving Tips
1. Use shorter prompts when possible
2. Set reasonable max_tokens limits
3. Start with gpt-3.5-turbo for learning
4. Monitor usage regularly

## 🔗 Helpful Resources

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Rate Limits Guide](https://platform.openai.com/docs/guides/rate-limits)
- [Token Counting](https://platform.openai.com/tokenizer)
- [Error Codes](https://platform.openai.com/docs/guides/error-codes)