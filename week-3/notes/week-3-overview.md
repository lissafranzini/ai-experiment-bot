# Week 3: AI Agents & Tool Use (Days 15-21)

## 🎯 Week Focus: From API Calls to AI Agents

This is where your learning path diverges from a typical AI course. Instead of just building utilities, you'll learn the patterns that underpin agentic AI systems - the foundation of your future career as an Agentic Workflow Manager.

## The Key Shift This Week

Until now, your code has been: you ask, AI answers. This week you'll build AI that **decides what to do on its own**.

```
Before (Weeks 1-2):    You → AI → Answer
This week (Week 3):    You → AI → [thinks] → [picks a tool] → [uses it] → [checks result] → Answer
```

## 📅 Daily Learning Path

### Day 15-16: API Integration Patterns & Function Calling
**The bridge between AI thinking and real-world action**
- RESTful API concepts and HTTP methods
- Working with JSON responses and structured data
- **Function calling**: How to give an AI tools it can use
- Rate limiting, retry logic, and error handling
- **Project**: Build an AI that can choose between multiple tools

### Day 17-18: Prompt Engineering for Agents
**Designing AI behavior, not just AI responses**
- System prompts that define agent roles and boundaries
- Few-shot learning and chain-of-thought prompting
- Temperature, top-p, and parameter tuning for reliability
- **Guardrails**: Constraining what an agent can and cannot do
- **Project**: Create a role-based AI assistant with defined boundaries

### Day 19-20: The Agent Loop
**Building your first autonomous AI agent**
- The ReAct pattern: Observe → Think → Act → Evaluate
- State management: Tracking what the agent has done
- Tool registration: Giving agents access to functions
- When to stop: Exit conditions and safety limits
- **Project**: Build a simple agent that can search, calculate, and answer questions

### Day 21: Week 3 Capstone - Your First Agent Application
**A complete tool-using AI agent**
- Command-line interface with argparse/typer
- Multiple tools the agent can choose from
- Logging every decision the agent makes
- Error handling and graceful failure
- **Project**: An AI research assistant that reads files, summarizes them, and answers questions

## 🧠 Core Concepts

### What Makes an Agent an Agent?

A regular AI script:
```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the weather in Paris?"
)
print(response.text)  # AI guesses based on training data
```

An AI agent:
```python
# The agent DECIDES to use a tool
# 1. AI reads the question
# 2. AI decides: "I need current data, let me use the weather tool"
# 3. AI calls: get_weather("Paris")
# 4. AI gets real data: {"temp": 18, "condition": "cloudy"}
# 5. AI formulates answer using real data
```

The difference: the agent **takes action in the real world** instead of just generating text.

### Function Calling (Tool Use)

This is the most important technical concept this week. You define tools as functions:

```python
def search_web(query: str) -> str:
    """Search the web for current information."""
    # Implementation here
    pass

def read_file(file_path: str) -> str:
    """Read and return the contents of a file."""
    with open(file_path, 'r') as f:
        return f.read()

def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    return str(eval(expression))
```

Then you describe these tools to the AI in a structured format. The AI decides which one to call based on the user's question. You execute the chosen function and return the result to the AI.

### The Agent Loop

```python
def agent_loop(user_task, tools, max_steps=10):
    messages = [{"role": "user", "content": user_task}]
    
    for step in range(max_steps):
        # 1. Ask AI what to do
        response = call_ai(messages, tools=tools)
        
        # 2. Check if AI wants to use a tool
        if response.wants_tool_call:
            # 3. Execute the tool
            result = execute_tool(response.tool_name, response.tool_args)
            
            # 4. Feed result back to AI
            messages.append({"role": "tool", "content": result})
        else:
            # 5. AI is done, return final answer
            return response.text
    
    return "Agent reached maximum steps without completing task"
```

This loop is the heart of every agentic system. Master it, and you understand the foundation of your future career.

### Guardrails

Agents can go wrong. Guardrails prevent that:

```python
class AgentGuardrails:
    max_steps = 10           # Don't loop forever
    max_tokens_per_step = 500  # Control costs
    allowed_tools = [...]    # Only these tools, nothing else
    require_approval = [     # Human must approve these
        "send_email",
        "delete_file",
        "make_purchase"
    ]
```

Designing guardrails is a core skill of an Agentic Workflow Manager.

## 🏗️ Week 3 Projects

### Project 1: Tool-Using AI (Days 15-16)
**Give an AI the ability to choose and use tools**

Build a script where the AI can:
- Search for information (simulated or real)
- Do calculations
- Read files from your computer
- The AI DECIDES which tool to use based on your question

### Project 2: Role-Based Assistant (Days 17-18)
**Design AI behavior through system prompts**

Create multiple "personalities" for the same AI:
- A strict code reviewer that only gives technical feedback
- A creative brainstorming partner that explores wild ideas
- A project manager that breaks tasks into actionable steps
- Each role has defined boundaries it cannot cross

### Project 3: Simple Agent (Days 19-20)
**Your first autonomous agent with the ReAct loop**

Build an agent that:
- Receives a research question
- Decides what information it needs
- Uses tools to gather that information
- Evaluates if it has enough to answer
- Loops back if it needs more
- Returns a final, well-supported answer

### Project 4: Research Assistant Agent (Day 21)
**Complete agent application with CLI**

Combine everything into a polished tool:
- Reads documents from a folder
- Answers questions about their contents
- Logs every decision and tool call
- Handles errors without crashing
- Runs from the command line

## 🎯 Learning Objectives

### By Day 17:
- [ ] Understand function calling / tool use concept
- [ ] Can define tools and let AI choose between them
- [ ] Implemented retry logic and error handling
- [ ] Understand the difference between AI calls and AI agents

### By Day 19:
- [ ] Can design system prompts that control agent behavior
- [ ] Understand guardrails and safety constraints
- [ ] Built role-based AI with defined boundaries
- [ ] Master prompt engineering for agent reliability

### By Day 21:
- [ ] Implemented the ReAct agent loop
- [ ] Built an autonomous agent with multiple tools
- [ ] Understand state management for agents
- [ ] Created a complete agent application

### Week End:
- [ ] Can explain the difference between AI tools and AI agents
- [ ] Built working agent with tool use and decision-making
- [ ] Understand guardrails and safety patterns
- [ ] Ready to think about multi-agent systems (Week 4)

## 📚 Why This Matters for Your Future

As an Agentic Workflow Manager, you'll need to:
- **Design** which tools each agent gets access to
- **Define** the boundaries and guardrails for each agent
- **Monitor** the decisions agents make in the loop
- **Optimize** how efficiently agents complete tasks
- **Debug** when agents make wrong decisions

This week gives you the hands-on experience of building these systems from scratch - which means you'll deeply understand them when you're managing them at scale in the future.

## 🔗 Resources

### Essential Reading
- [ReAct: Reasoning and Acting in Language Models](https://react-lm.github.io/) - The foundational paper
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) - How tool use works
- `resources/agentic-ai-landscape.md` - Your reference guide to the agent ecosystem

### Frameworks (read about, don't use yet)
- LangChain / LangGraph
- CrewAI
- AutoGen

Understanding the concepts manually first makes these frameworks much easier to learn later.

**Week 3 transforms you from someone who uses AI into someone who builds AI agents. This is the foundation of your Agentic Workflow Manager career.**