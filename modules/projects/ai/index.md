---
uid: AI
---

# AI

## Overview

The **AI system in @@name** introduces intelligent automation and natural language capabilities directly within the ERP platform.  
It enables users to interact with **AI Assistants**, **AI Chat Arbiters**, and **AI-powered business logic**, seamlessly integrated into daily workflows.

@@name’s AI functionality is built on an **external provider model** (currently supporting **OpenAI’s models**).  
This means ERP.net connects securely to OpenAI’s API to generate, process, and analyze natural language, but the architecture is **extensible** — designed to accommodate other AI providers in the future.

AI Models in @@name are **hierarchical**, allowing each model to inherit context and knowledge from parent models.  
This structure supports both **company-wide master models** and **specialized assistants** for specific departments or workflows (for example, Marketing AI or Sales AI).

The models based on OpenAI’s technology can also be **fine-tuned and trained** directly within @@name, using the company’s own data, procedures, and best practices.  
This enables the AI to understand the unique rules, terminology, and business logic of each organization, providing tailored and context-aware assistance.

By embedding this technology throughout ERP.net, users can:

- Chat with an **AI Assistant** directly inside the application.  
- Involve AI as a **Chat Arbiter** in group or private conversations.  
- Use AI in **form panels** to analyze, explain, or generate business data.  
- Automate and validate operations through **AI-enhanced business rules**.  
- Employ AI-powered tools such as **document ingestion**, **lead creation**, and **intelligent task generation**.

The goal is to make AI a **natural and context-aware part of everyday ERP processes**, improving accuracy, speed, and decision-making across all departments.

## 2. Architecture

The AI functionality in ERP.net is built as a modular system, consisting of several entities that define configuration, training, and runtime behavior.  
Together, they form a complete framework for integrating and managing AI models within the ERP environment.

| Entity | Description |
|--------|--------------|
| **Providers** | Define connections to external AI services (currently only OpenAI). Store API credentials, provider type, and base model configuration. |
| **Models** | Define the individual AI models available in the system. Models can be **hierarchical**, meaning a model can inherit knowledge and settings from a parent model. Each model can represent a specific assistant (e.g. Marketing AI, Sales AI) or a company-wide master model.
| **ModelQAs** | Store structured Question & Answer pairs for model fine-tuning. Used to teach the model company-specific rules and best practices. |
| **TrainingConversations** | Contain conversational training sessions used to improve model behavior. Created through real user– AI chat arbiter interactions using the "Train AI" function |
| **TrainingConversationMessages** | Store the individual messages from each training conversation. Used during model compilation to provide contextual learning data. |
| **Compilations** | Track the process of compiling and deploying trained models. Each successful compilation results in a ready-to-use AI instance. |
| **CompilationAssets** | Contain the assets (instructions, data, and context) used during a compilation. Provide the resources that define the model’s learning scope. |
| **AssistantConversations** | Store user conversations with AI Assistants within ERP.net. Maintain a history of interactions and ensure data security. |


