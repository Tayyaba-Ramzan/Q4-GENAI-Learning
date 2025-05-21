![OpenAI Agents Banner](https://composio.dev/wp-content/uploads/2025/03/agents-sdk-min.png)

# 🚀 Exploring OpenAI Agents SDK

This task focuses on understanding the architecture of the OpenAI Agents SDK and answering thought-provoking questions about its internal design — including the `Agent`, `Runner`, and generics like `TContext`.

---

## 📘 Medium Blog

For a complete breakdown with clear explanations, examples, and links to documentation, read the full blog post here:

👉 [🔗 Read the Full Blog on Medium](https://medium.com/@tayyabaramzan.it/exploring-openai-agents-sdk-understanding-agent-runner-and-generics-d54a9f149856) 

---

## 🧠 Questions Covered

### 1. Why is the `Agent` class defined as a `dataclass`?

- Used for clean, minimal configuration setup
- Automates `__init__`, `__repr__`, and comparisons
- Ideal for holding agent instructions, tools, and other attributes

---

### 2. Why is the system prompt stored in the `Agent` class as `instructions`?

- Can be static (`str`) or dynamic (`callable`)
- Allows system prompt customization based on runtime context

---

### 3. Why is the user prompt passed to the `Runner.run()` method and why is it a `@classmethod`?

- `run()` handles live user input
- It’s a class method because it orchestrates a stateless flow (no instance needed)

---

### 4. What is the purpose of the `Runner` class?

- Controls the execution of agent logic
- Bridges the agent’s tools, prompts, and output response
- Coordinates everything in a clean lifecycle

---

### 5. What are Generics in Python and why is `TContext` used?

- Python `TypeVar` enables flexible type-safe context
- `TContext` allows agents to define their own structure of context data
- Makes the system extensible while preserving type safety

---

## 📎 References

- [Agent Class – OpenAI SDK Docs](https://openai.github.io/openai-agents-python/ref/agent/)
- [Runner Class – OpenAI SDK Docs](https://openai.github.io/openai-agents-python/ref/run/)
- [Dataclasses – Python Official Docs](https://docs.python.org/3/library/dataclasses.html)
- [Typing and Generics – Python Docs](https://docs.python.org/3/library/typing.html)

---

## ✨ Summary

This task deepens your understanding of how OpenAI Agents work under the hood. By analyzing design choices like dataclasses, callables, class methods, and generics, you gain architectural insight that helps you build scalable AI applications.

> _“Code is easier to write when you understand the architecture it lives in.”_

---

🧑‍💻 Happy Learning & Keep Exploring AI Agents!
