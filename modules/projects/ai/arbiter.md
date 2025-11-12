# AI Arbiter

## 1. Overview

The **AI Arbiter** is an AI model that participates as a **member in ERP.net chats**.  
It acts like a virtual colleague who can:

- answer questions inside a group conversation,
- clarify or check information (“who is right here?”),
- summarise long discussions,
- suggest next steps or rewrite texts.

The arbiter uses an **AI Model** and speaks through a **Virtual User** that appears as a normal chat participant.

## 2. Prerequisites

To use an AI Arbiter, you need:

1. **AI infrastructure configured**
   - AI Server site (infrastructure prerequisite).
   - At least one **AI Provider** (OpenAI) with API key.
   
2. **Virtual User**
   - One **Virtual User (No login)** that will represent this model in chats.
   - Each Virtual User can be linked to **only one** AI model.

3. **AI Model for the arbiter**
   - A record in `AI Models`.
   - Usually with:
     - `Build assistant = null`  
       (so the model can be fine-tuned with Q&A and Training Conversations).
   - Linked to an AI Provider (base model in OpenAI).
   - Specified Virtual User - the one created in step 2.
  
**For more info on steps from 1 to 3, see  [How to - Setup AI](./how-to/setup-ai.md)**

4. (Optional) **Fine-tuning**
   - System Message for general behaviour and tone.
   - Q&A entries (Model Q&As).
   - Training Conversations (including those created via **Train AI** from chats).

5. (Optional, if fine-tuned) **Model compilation**  
   - Required if you use Q&A / Training Conversations or want a dedicated assistant configuration.
   - See: *AI Setup – Model compilation* in the main docs.

**For more info on steps from 4 to 5, see  [How to - Fine-tune AI Models](.fine-tune-models.md)**

## 3. Configuring the AI Arbiter in a chat

1. Open the desired **chat group** (e.g. *Marketing*, *Sales*, *Support*).
2. Open the **Members** / participants list.
3. Add the **Virtual User** linked to your arbiter model as a member of the group.

From this moment, the AI Arbiter is available in that chat.


## 4. Using the AI Arbiter

Inside the chat group where the arbiter is a member, users can:

- Ask questions directly in the channel  
  e.g. “@Marketing AI, how often should we post on Instagram?”  
- Ask it to review a message or thread  
  e.g. “@AI, is this proposal consistent with our pricing rules?”  
- Ask for a summary  
  e.g. “@AI, summarise today’s discussion and list next steps.”

The arbiter bases its answers on:

- the **current conversation context** in the chat,
- any **fine-tuning** (System Message, Q&A, Training Conversations) configured for its model,
- the general knowledge of the underlying OpenAI model.


## 5. Training the Arbiter from real conversations (Train AI)

When the arbiter gives an answer that is not entirely correct or could be improved, you can:

1. Correct or refine the answer in the chat (explain what is right).
2. When you reach a good version, open the context menu on the AI’s message and choose **Train AI**.
3. Select which messages from the conversation should be included.
4. Confirm.

ERP.net will create a **Training Conversation** for the arbiter’s model.  
After the next compilation (if used), the arbiter will use this new knowledge in future answers.


## 6. Notes and good practices

- Create **separate arbiters** for different domains (e.g., Marketing, Sales) if their knowledge and tone should differ.
- Keep the System Message short and focused (“You are a marketing assistant for ERP.BG…”).
- Use Q&A for fixed rules and policies, and Training Conversations for real examples.
- Only add the arbiter to groups where it is actually useful, to avoid unnecessary noise.

The AI Arbiter turns your chat groups into **smart, context-aware rooms** where AI can actively support discussions instead of being a separate tool.
