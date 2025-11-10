# Setup AI

## 2. Configuration

This section describes all system-level settings required to enable AI in ERP.net:

1. AI Server site 
2. AI Providers - requires an active **OpenAI account** and an API key. All API usage is billed **directly by OpenAI** under that account.
3. AI Models  
4. Model compilation and updates  
5. Assigning a model to each user

Once these are configured, end users can work with AI Assistants, chat arbiters, business rules and Ingest without needing to know any technical details.

---

### 2.1 AI Server Site (infrastructure prerequisite)

> ℹ️ **What is this?**  
> The AI Server site is a small, one-time configuration that prepares your ERP instance for the newer AI architecture.  
> It is required at system level, but it is **not something end users interact with directly**, and it does not change how the existing AI features are used.

Starting from **ERP.net version 26**, each instance must have an **AI Server site** defined.  
This site acts as an internal endpoint that ERP.net will use more and more in future versions to route AI calls in a standardized way.

At the moment, the AI Server site is primarily **infrastructure** – it must be present and correctly configured, but the visible AI functionality (assistant panel, chat arbiters, Q&A training, etc.) continues to work in the same way from the user’s perspective.

#### 2.1.1 Creating the AI Server Site

1. Open **Navigator → Web Sites**.
2. Click **New** to create a new web site record.
3. Set **Type** to `WebServerSiteTypeAIServer`.
4. The **Relative URL** will be filled automatically based on the instance name.
5. Click **Save**.

> ✅ This is usually all that is needed.  
> Once saved, the ERP instance is considered “AI-ready” from an infrastructure standpoint.

Make sure your license includes at least one site — the AI Server site uses the standard site licensing.

#### 2.1.2 Trusted Application (only if needed)

In most installations, no additional configuration is required.

If you encounter authentication issues, you can create a **Trusted Application** for the AI Server site:

1. Open the AI Server Site record.
2. Click **Create Trusted Application**.
3. Save.

ERP.net will generate the necessary credentials automatically.  
Again, this is a **technical safety net** and not something normal users will ever work with.

---

### 2.2 AI Providers

After the AI Server site is configured, the next step is to define at least one **AI Provider**.  
A provider represents an external AI service – currently, **OpenAI**.

Each company typically defines **a single provider** pointing to its OpenAI account.

#### 2.2.1 Required fields

In **Projects.AI.Providers**:

- **Name** – a descriptive name (e.g. “OpenAI – Production”).
- **Provider** – `OpenAI` (currently the only supported option).
- **Base model name** – the default model to use, e.g. `gpt-4o-mini`, `gpt-4o`, etc.
- **Provider API key** – the secret API key from the company’s OpenAI account.

> 💡 The API key is created in the **OpenAI dashboard → API keys**.  
> Copy the value once and paste it into the Provider record in ERP.net.

Billing for AI usage is handled **directly by OpenAI** according to the company’s usage and pricing plan.

---

### 2.3 AI Models

An **AI Model** in ERP.net represents a concrete assistant configuration:

- which provider and base model it uses,
- what system instructions it follows,
- what training data it is connected to,
- and whether it is available in the assistant panel, in chats, or in both.

You can define **multiple models** – for example:

- “Company Master Assistant”
- “AI Marketing Assistant”
- “AI Sales Assistant”
- “AI Developer Helper”

#### 2.3.1 Key fields (Projects.AI.Models)

- **Name**  
  Human-readable model name, e.g. `AI Marketing Assistant`.

- **Parent** (optional)  
  Used to build a **hierarchical structure** of models.  
  A parent model can aggregate training from its children, which is useful for a “master” company-wide assistant.

- **Virtual User**  
  A **Virtual User** whose identity the model uses in chats and the assistant panel.  
  This is the “user” you see in group chats when the AI answers.

- **System message**  
  Global instructions that always apply to the model, such as:
  - tone of voice (formal / informal),
  - language preferences,
  - how to address users,
  - specific company naming conventions, etc.

  Keep this short and focused – typically up to 1–2 pages of text at most.

- **Conversation compilation**  
  Reference to the **latest successful compilation** that the model uses at runtime.  
  This field is maintained automatically after each compile.

- **Default model**  
  Marks this model as the **system default**.  
  System-level AI actions (e.g. business rules) use the default model when no user-specific model is assigned.  
  Only **one** model can be default at a time.

- **Build assistant**  
  Controls how this model is used:
  - `Yes` → the model is used as an **assistant** in the AI Assistant app and assistant panels in forms.  
    In this mode, it does **not** use Q&A / training conversations for fine-tuning.
  - `null` / not checked → the model can be **fine-tuned** with:
    - Q&A records, and
    - Training Conversations.  
    These models are typically used as **chat arbiters** in channels or as specialized assistants.

- **Provider**  
  Links the model to one of the configured **AI Providers**, and therefore to a specific base model and billing account.

---

### 2.4 Model Compilation

Once a model is configured, it must be **compiled** before it can be used.

Compilation sends the model’s configuration and training data to the AI provider and creates a runnable assistant configuration there.

#### 2.4.1 Running a compilation

From an AI Model record:

1. Open the model in edit mode.
2. Use **Run → Compile** (or the corresponding action).
3. Wait for the compilation to complete.

The result of each compilation is stored in **Projects.AI.Compilations** and visible in the model:

- **Successful** compilations update the `Conversation compilation` field.
- **Failed** compilations leave the previous version active and provide diagnostics.

#### 2.4.2 Logs and error diagnostics

If a compilation fails:

- Check **Error message** in the model – it usually contains the main reason (e.g., invalid base model name).
- Check **Build log** – for more detailed, technical information.

You can correct the configuration and run the compilation again.  
Existing, previously compiled versions continue to work until a new compilation succeeds.

> ⏱ Compilation time can vary:  
> - Simple assistant models: usually a few minutes.  
> - Models with many Q&A and Training Conversations: can take longer, depending on data size.

---

### 2.5 Assigning a Model to Users

Finally, each user who will work with AI should be connected to a specific AI model.

#### 2.5.1 User configuration

1. Open **Users**.
2. Open the user’s record (e.g. `Admin`).
3. In the **Model** field, select the desired AI Model.

This model will be used:

- in the **AI Assistant app**,
- in **assistant panels** inside forms,
- and, in many cases, as the default model in that user’s AI interactions.

If no model is assigned to a user, the system may fall back to the **Default model**, but it is recommended to explicitly configure a model for all users who are expected to use AI.

> 🔒 All AI Assistant conversations are user-specific and protected by the ERP.net security system.  
> One user cannot see another user’s assistant conversations.
