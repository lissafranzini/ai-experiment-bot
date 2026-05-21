# Week 4: Multi-Agent Systems & Human-AI Collaboration (Days 22-28)

## 🎯 Week Focus: Orchestrating Agent Teams

Last week you built a single agent. This week you'll build systems where **multiple agents work together** - and where **humans stay in the loop** when it matters. This is the core of what an Agentic Workflow Manager does.

## The Big Picture

```
Week 3: One agent, multiple tools
Week 4: Multiple agents, working as a team
```

A single agent hits a ceiling. Complex tasks need specialists:
- One agent is great at research
- Another is great at writing
- Another is great at reviewing
- A manager decides who does what and when

Sound familiar? It's how human teams work too. Your future job is designing these digital teams.

## 📅 Daily Learning Path

### Day 22-23: Multi-Agent Architecture
**Designing agent teams**
- Why single agents aren't enough for complex tasks
- Agent roles and specialization patterns
- Communication between agents: message passing
- Sequential vs parallel agent execution
- **Project**: Build a two-agent system (researcher + writer)

### Day 24-25: Human-in-the-Loop Workflows
**Knowing when AI should stop and ask a human**
- Approval workflows: AI proposes, human decides
- Confidence thresholds: When is the agent unsure?
- Escalation patterns: Routing to the right human
- Feedback loops: Humans teaching agents to improve
- **Project**: Build an agent workflow with human checkpoints

### Day 26-27: State, Memory, and Persistence
**Agents that remember and learn**
- Conversation history and context management
- SQLite for storing agent decisions and outcomes
- Shared state between multiple agents
- Audit trails: Logging what every agent did and why
- **Project**: Multi-agent system with persistent memory and audit log

### Day 28: Orchestration Patterns
**The workflow manager's toolkit**
- Pipeline pattern: Agent A → Agent B → Agent C
- Fan-out/fan-in: Multiple agents work in parallel
- Router pattern: A manager agent delegates to specialists
- Error recovery: What happens when an agent fails?
- **Project**: Design and build a complete agentic workflow

## 🧠 Core Concepts

### Multi-Agent Communication

Agents need a way to pass information to each other:

```python
class AgentMessage:
    sender: str      # Which agent sent this
    receiver: str    # Which agent should receive it
    content: str     # The actual message
    task_id: str     # Which task this belongs to
    status: str      # "pending", "in_progress", "completed", "failed"
```

### Orchestration Patterns

#### 1. Sequential Pipeline
Each agent does its job and passes the result to the next:
```
User Request → [Research Agent] → [Writer Agent] → [Review Agent] → Final Output
```
Simple, predictable, easy to debug. Start here.

#### 2. Router / Manager Pattern
A manager agent reads the task and decides who handles it:
```
User Request → [Manager Agent]
                    │
              ┌─────┼─────┐
              ▼     ▼     ▼
         [Agent A] [Agent B] [Agent C]
              │     │     │
              └─────┼─────┘
                    ▼
              [Manager Agent] → Final Output
```
More flexible, but harder to debug.

#### 3. Fan-Out / Fan-In
Multiple agents work on different parts simultaneously:
```
User Request → [Splitter]
                  │
            ┌─────┼─────┐
            ▼     ▼     ▼
         [Agent] [Agent] [Agent]   ← all work in parallel
            │     │     │
            └─────┼─────┘
                  ▼
             [Combiner] → Final Output
```
Fastest, but requires careful coordination.

### Human-in-the-Loop Patterns

#### Approval Gate
```
Agent does work → Presents result → Human approves/rejects → Continue or redo
```

#### Confidence Threshold
```python
if agent.confidence < 0.7:
    result = ask_human(agent.draft_response)
else:
    result = agent.draft_response
```

#### Escalation
```
Agent tries → Fails or uncertain → Routes to human expert → Human resolves
```

#### Feedback Loop
```
Agent produces output → Human rates quality → Agent adjusts approach → Better next time
```

As an Agentic Workflow Manager, deciding WHERE to place these human checkpoints is one of your most important design decisions. Too many = slow and expensive. Too few = risky and unreliable.

### State Management

When multiple agents collaborate, they need shared state:

```python
class WorkflowState:
    task_id: str
    status: str                    # "in_progress", "completed", "failed"
    current_agent: str             # Who's working on it now
    history: list                  # What's been done so far
    shared_context: dict           # Information all agents can access
    human_decisions: list          # Record of human interventions
    created_at: datetime
    updated_at: datetime
```

### Audit Trails

In production agent systems, you MUST log everything:
- What decision did each agent make?
- What tools did it call?
- What was the result?
- How long did it take?
- How many tokens did it use?

This isn't just for debugging. It's for **accountability**. When an agent makes a mistake, you need to understand why.

## 🏗️ Week 4 Projects

### Project 1: Two-Agent Pipeline (Days 22-23)
**Your first multi-agent system**

Build a research-and-write pipeline:
- **Research Agent**: Takes a topic, gathers information, produces structured notes
- **Writer Agent**: Takes research notes, produces a polished summary
- **Orchestrator**: Connects them together, passes data between them

Start simple. Two agents, one direction. Get the communication working.

### Project 2: Human-in-the-Loop Workflow (Days 24-25)
**AI that knows when to ask for help**

Build a content creation workflow:
- Agent drafts content based on a prompt
- System evaluates the output (length, format, key points)
- If below quality threshold → presents to human for feedback
- Human can approve, reject, or provide guidance
- Agent incorporates feedback and tries again

The insight: the human doesn't do the work, but they steer the quality.

### Project 3: Stateful Agent System (Days 26-27)
**Agents with memory and accountability**

Add persistence to your multi-agent system:
- SQLite database stores every agent action
- Agents can reference what previous agents did
- Dashboard shows the workflow history
- Can resume a workflow after interruption
- Full audit trail of every decision

### Project 4: Complete Agentic Workflow (Day 28)
**Your signature orchestration project**

Build a 3+ agent workflow for a real use case:
- Manager agent that routes tasks
- Specialist agents that handle subtasks
- Human approval gate for critical decisions
- Persistent state and audit logging
- Error handling and retry logic

Example use cases:
- **Report Generator**: Research → Analyze → Write → Review → Approve
- **Code Assistant**: Understand → Plan → Implement → Test → Review
- **Content Pipeline**: Ideate → Draft → Edit → Format → Publish

## 🎯 Learning Objectives

### By Day 24:
- [ ] Built a working two-agent pipeline
- [ ] Understand message passing between agents
- [ ] Can design sequential and parallel workflows
- [ ] Grasp the difference between orchestration patterns

### By Day 26:
- [ ] Implemented human-in-the-loop checkpoints
- [ ] Understand confidence thresholds and escalation
- [ ] Can design approval workflows
- [ ] Know when to involve humans vs let agents decide

### By Day 28:
- [ ] Built persistent state management for agents
- [ ] Implemented audit logging for agent decisions
- [ ] Created a complete multi-agent workflow
- [ ] Understand error recovery in agent systems

### Week End:
- [ ] Can design multi-agent architectures
- [ ] Understand orchestration patterns and trade-offs
- [ ] Know how to balance automation with human oversight
- [ ] Have a working multi-agent system in your portfolio

## 📚 Why This Matters for Your Future

This week is the most directly relevant to your Agentic Workflow Manager goal:

| What you build this week | What you'll do at scale in 5 years |
|---|---|
| 2-3 agents passing messages | Ecosystems of dozens of specialized agents |
| Simple approval gates | Sophisticated human-AI collaboration frameworks |
| SQLite audit logs | Enterprise monitoring and observability platforms |
| Basic orchestration | Complex workflow engines with failover and recovery |

The patterns are identical. The scale changes.

## 🔗 Resources

### Essential Reading
- `resources/agentic-ai-landscape.md` - Agent ecosystem overview
- [Multi-Agent Systems Overview](https://www.deeplearning.ai/short-courses/) - DeepLearning.AI courses
- [Human-in-the-Loop ML](https://humanloop.com/blog) - Practical HITL patterns

### Frameworks (awareness, not mastery)
- **LangGraph**: Graph-based agent orchestration
- **CrewAI**: Multi-agent collaboration framework
- **AutoGen**: Microsoft's multi-agent framework

You'll dive deep into these frameworks after Day 30. For now, building from scratch teaches you what these frameworks do under the hood.

**Week 4 is where you start thinking like an Agentic Workflow Manager - designing systems where AI agents and humans collaborate effectively.**