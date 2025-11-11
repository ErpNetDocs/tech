## Fine-tune AI Models in @@name

### 1. What is fine-tuning?

Fine-tuning in @@name means **adapting a base AI model** (from OpenAI) to your company’s specific rules, language and way of working.

Instead of using a general model that “knows a bit of everything”, you can train specialized assistants such as:

- “AI Marketing Assistant”
- “AI Sales Assistant”
- “AI Support Assistant”
- A company-wide “Master Assistant”

Fine-tuning is done entirely inside @@name, using:

- **System message** – general instructions and behaviour.
- **Q&A records** – structured questions and answers.
- **Training conversations** – real chat dialogues that the model has “learned from”.

The result is a model that understands your processes, terminology, and internal rules much better than a generic ChatGPT.

---

### 2. When do you need fine-tuning?

Fine-tuning is recommended when:

- You want an assistant who **knows your internal procedures**, not just generic best practices.
- You want different models for different departments (Marketing, Sales, Support, etc.).
- You want the model to give **consistent** answers in line with your company policies.

From a technical perspective, fine-tuning is needed when:

- You want to use a **fine-tuned model** (Q&A and/or Training Conversations).
- You want to use a **dedicated AI Assistant** (the *My Assistant* app or assistant panel) with its own behaviour.

In all other scenarios (for example, simple backend AI rules without specialization), @@name can work directly with the **base model** from the AI Provider without fine-tuning.

---

### 3. Prerequisites

Before fine-tuning a model, make sure you have:

1. **AI Server Site** configured (infrastructure prerequisite).
2. At least one **AI Provider** (OpenAI) with a valid API key.
3. An **AI Model** created in `Projects.AI.Models`:
   - `Build assistant = null` if you plan to use Q&A and Training Conversations.
   - A linked **Provider** (OpenAI).
4. (Optional, but typical) a **Virtual User**, if the model will be used in chats or the My Assistant app.

---

### 4. Fine-tuning components

Fine-tuning in @@name is built from three main elements:

#### 4.1 System message

The **System message** field in the AI Model contains high-level instructions that always apply.

Typical examples:

- “Answer briefly and clearly.”
- “Always use the English language in replies, unless explicitly asked otherwise.”
- “Refer to the company as ‘ERP.BG’ in all messages.”
- “You are a marketing assistant for ERP.BG. You help with social media posts, newsletters, and campaign ideas.”

Good practices:

- Keep it **focused and concise** (up to 1–2 pages of text).
- Describe **role, tone, language, constraints**.
- Avoid including long policy documents here – those are better suited as Q&A or Training Conversations.

---

#### 4.2 Q&A (Projects.AI.ModelQAs)

**Q&A records** define explicit question–answer pairs that the model should know.

They are ideal for:

- Internal rules and policies
- Standard operating procedures
- Repetitive “how do we do X in our company?” questions

Examples:

- **Question:** “How often should we post on Instagram?”  
  **Answer:** “Our marketing team posts 4 times per week, with a mix of product, educational, and customer-story posts.”

- **Question:** “What is our rule for collecting e-mails for the newsletter?”  
  **Answer:** “We always ask for explicit consent and follow GDPR opt-in rules…”

When a user asks something similar, the model uses the Q&A data to give an answer that follows your **exact internal rule**, not generic advice.

---

#### 4.3 Training Conversations (Projects.AI.TrainingConversations)

**Training Conversations** let you fine-tune the model using **real chat dialogues**.

They are especially useful when:

- You discover the model makes a recurring mistake.
- You want to teach a new topic in a natural, conversational way.
- You prefer to train “while working”, instead of writing static Q&A.

There are two ways to create Training Conversations:

1. **Manually** – by creating records in `Projects.AI.TrainingConversations` and `TrainingConversationMessages`.
2. **Automatically from chat** – using the **Train AI** command.

##### 4.3.1 Training from chat (Train AI)

When you are chatting with the AI in a group or direct chat:

1. Ask the model a question.
2. If the response is wrong or incomplete, correct it in the chat (explain what is actually correct).
3. When you reach a good answer, right-click (or use the context menu) on the AI’s message and choose **Train AI**.
4. Select which messages from the conversation should be included.
5. Confirm.

@@name will:

- Create a new **Training Conversation** for the corresponding model.
- Store the relevant messages as **Training Conversation Messages**.
- Mark the conversation as available for the next compilation.

This allows you to **improve** the model continuously while using it, without having to pre-invent hundreds of Q&A pairs.

---

### 5. Model hierarchy and reuse

The **Parent** field in the AI Model allows you to build a **hierarchy of models**.

Typical pattern:

- **Master Company Model**  
  Parent: *null*  
  Trained on: general company knowledge, policies, and products.

- **Marketing Model**  
  Parent: *Master Company Model*  
  Trained on: marketing-specific Q&A and conversations.

- **Sales Model**  
  Parent: *Master Company Model*  
  Trained on: sales-specific Q&A and conversations.

The parent can aggregate and reuse training from its children (according to your configuration), so you do not need to copy the same base knowledge to every model.  
This is especially useful for a **company-wide assistant** for managers or general users.

---

### 6. Compilation and applying the fine-tuning

After you add or change the System Message, Q&A, or Training Conversations, you must **compile** the model so the changes are applied at the AI provider.

#### 6.1 When compilation is required

Compilation is required in only two cases:

- when you want to use a **fine-tuned model** (Q&A and/or Training Conversations), or  
- when you want to use a dedicated **AI Assistant** (the *My Assistant* app or assistant panel).

In all other scenarios, @@name works directly with the **base model** defined in the AI Provider and does not require compilation.

#### 6.2 Running a compilation

From an AI Model record:

1. Open the model.
2. Start **Compile** (via the Run menu or the corresponding action).
3. Monitor the result in the **Compilations** sub-panel or via the **Notifications** panel:
   - The **Status** column shows the progress (e.g., `Queued`, `Running`, `Completed`).
   - The **Is Successful** flag indicates if the compilation has finished successfully.

If the compilation is successful, the **Conversation compilation** field is updated and the new fine-tuned version becomes active.

If the compilation fails:

1. Check the **Is Successful** flag and **Status**.
2. Review the **Error Message** for the main cause (e.g., invalid or unsupported base model).  
   Hover over it to see the full text.
3. If necessary, open the **Build Log** to inspect technical details.

You can adjust the configuration and run the compilation again.  
Existing, previously successful compilations remain active until a new compilation completes successfully.

---

### 7. Using a fine-tuned model

Once a fine-tuned model is compiled, it can be used:

- as an **arbiter** in chats (added as a member to relevant groups, e.g. Marketing group),
- as the model behind a specific **Virtual User**,
- as the model assigned to users for:
  - the **AI Assistant app** (My Assistant),
  - **assistant panels** in forms.

Which users see which behaviour depends on:

- which **model** is assigned in their **User** record (for assistants),
- and which **Virtual User / AI model** is configured for a chat group (for arbiters).

---

### 8. Best practices for fine-tuning

- Start with a **small scope** – for example, one model for a single department.
- Keep System messages **short and clear**.
- Use Q&A for **fixed rules** and **policies**.
- Use Training Conversations for **real-world examples** and recurring issues.
- Train gradually using **Train AI** during actual work.
- Compile only when there are meaningful changes (to avoid unnecessary waiting).
- Document internally which model is used for which purpose (Marketing, Sales, etc.).

Fine-tuning is not a one-time project – it is an **ongoing process**.  
Over time, as you add more Q&A and Training Conversations, your assistants will become more accurate, more “on brand”, and much more useful for your users.
