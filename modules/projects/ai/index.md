---
uid: AI
---

# AI

## What is @@name AI?

@@name AI brings smart assistants and functions directly into your ERP, so people can:

- Ask questions in chat instead of clicking through menus.
- Let AI read and explain project data, tasks, and documents.
- Automate routine work – from creating leads to validating business rules.

Under the hood, @@name connects securely to external AI providers (currently OpenAI).
You choose which models to use, what they are allowed to know, and where they can help in your processes.

AI Models in @@name are **hierarchical**, allowing each model to inherit context and knowledge from parent models.  
This structure supports both **company-wide master models** and **specialized assistants** for specific departments or workflows (for example, Marketing AI or Sales AI).

The models based on OpenAI’s technology can also be **fine-tuned and trained** directly within @@name, using the company’s own data, procedures, and best practices.  
This enables the AI to understand the unique rules, terminology, and business logic of each organization, providing tailored and context-aware assistance.

By embedding this technology throughout @@name, users can:

- Chat with an **AI Assistant** directly inside the application.  
- Involve AI as a **Chat Arbiter** in group or private conversations.  
- Use AI in **form panels** to analyze, explain, or generate business data.  
- Automate and validate operations through **AI-enhanced business rules**.  
- Employ AI-powered tools such as **document ingestion**, **lead creation**, and **intelligent task generation**.

The goal is to make AI a **natural and context-aware part of everyday ERP processes**, improving accuracy, speed, and decision-making across all departments.

> [!NOTE]
>
> 💡 **Using OpenAI with ERP.net**
> 
> ERP.net AI features use the OpenAI API behind the scenes.
> - Each customer creates their own OpenAI account and API key.
> - OpenAI bills you directly based on your usage.
> 
This keeps ERP.net transparent about costs and allows you to control your AI budget.


## 2. Architecture

ERP.net AI is a modular system. You plug in an external AI provider, define one or more
AI models (assistants), teach them with your data, and then use them in chats, forms,
and business rules.

### Key building blocks

**Providers**  
*Think of this as the “connection” to an AI service.*  
- Stores the API credentials and base model (e.g., OpenAI GPT model).
- Configured once per AI provider.

**Models**  
*Your actual AI assistants.*  
- Each model represents a specific assistant (e.g,. “Project AI”, “Sales AI”, “Master AI”).
- Models can inherit settings and knowledge from a parent model.

**ModelQAs**  
*Structured Q&A knowledge base.*  
- Store question–answer pairs with your company rules and best practices.
- Used to fine-tune how the model answers typical questions.

**TrainingConversations & TrainingConversationMessages**  
*Real chats used as training examples.*  
- Capture real user ↔ AI interactions (via “Train AI”).
- Used during compilation to teach the model how your users talk.

**Compilations & CompilationAssets**  
*Turning training data into a ready-to-use AI*  
- Compilations bundle instructions, data, and context.
- A successful compilation produces a deployable AI model version.

**AssistantConversations**  
*Day-to-day user chats with AI*  
- Store the conversation history between users and AI assistants.
- Ensure auditability and data security.


