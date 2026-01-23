# AI Assistant in @@name

AI Assistant in ERP.net is designed to help users **directly in the context of their work** – without copying data, without switching between systems, and without relying on external tools.

It is not just a generic AI chat, but a deeply integrated assistant that:

* understands where you are in the system;
* can work with the data from the current screen;
* respects ERP.net access permissions;
* can be trained according to real company processes.


## What is the @@name AI Assistant?

AI Assistant is a conversational interface embedded in ERP.net, created to support users in their daily tasks.

Instead of searching through documentation or manually formatting text, you can ask AI Assistant to:

* explain the data from the current record;
* summarize information;
* generate text (for example, a User Story);
* validate content.

A key aspect is that the AI Assistant **can work within the current context**.


## Where can the AI Assistant be used?

AI Assistant is available in two main places within ERP.net.

### AI Assistant Application

A standalone application accessible from **My Apps**.

It is suitable for:

* general questions;
* quick lookups;
* work without a specific record open.

The application can be pinned for quick access at any time.

![Assistant App](assistant_app.png)


### AI Assistant Side Panel

The AI Assistant Side Panel is available in all entity definitions and navigators.

This is the most commonly used way to work with the assistant because:

* it has access to the current record;
* it can work with real on-screen data;
* it supports concrete tasks as part of the working process.

The panel is opened from the three-dot (overflow) menu and can be:

* minimized;
* maximized;
* expanded to full screen.

![Assistant Side Panel](assistant_side_panel.png)


## Conversations, privacy, and security

Every conversation with the AI Assistant is **personal**.

This means that:

* each user sees only their own conversations;
* conversations are not visible to other users;
* security is enforced by the ERP.net security system.

Even when multiple users work with the same model, their conversations and context remain fully isolated.


## Working with context: Get Data

One of the strongest capabilities of the AI Assistant is its ability to work with the context of the current screen.

When working with a specific record (for example, a Feature, Case, or Document), you can use the **Get Data** button.

It:

* extracts the relevant data from the currently opened record;
* sends it to the AI Assistant as context;
* allows the assistant to base its responses on real data.

Typical scenarios include:

* generating a User Story from a Feature;
* summarizing a record;
* validating whether the data is filled in correctly.

![Assistant Get Data](assistant_get_data.png)

---

## Starting fresh: New Conversation

Over time, the AI Assistant accumulates context from the conversation.

In some cases, this is not desirable – for example, when:

* you change the topic;
* the assistant starts producing inaccurate responses;
* you want a clean start.

In such situations, use **New Conversation**.

This function:

* clears the current conversation history;
* removes the accumulated context;
* starts a new conversation.

![New Conversation](assistant_new_convo.png)

## Additional Instructions

Additional Instructions allow you to control how AI Assistant behaves and how it formats its answers — without changing or retraining the underlying model.

This functionality is especially useful when you want the assistant to:

* follow a specific tone or style;

* respond in a predefined format;

* interpret attached files in a particular way;

* apply consistent rules across conversations.

Additional Instructions are **not training**. They do not change the model itself and are applied only as guidance during the conversation.

### How to use them

Open the AI Assistant panel menu (⋮) and select Additional Instructions.

This opens a window where you can:

* Review the instructions to understand how the assistant is currently configured

* Edit them to better match your needs. Add your own rules, for example:

- ask for shorter answers

- change the tone

- define how the assistant should react to certain questions

* Experiment freely 

After saving, the assistant will immediately use your instructions for your assistant conversations.

If you clear the text, the assistant will automatically continue using the default instructions.


## Teaching the Assistant: the right way

AI Assistant **cannot be trained using Q&A**.

This is a key architectural principle.

### Training Conversations (Train AI)

The only supported way to train AI Assistant is through **Training Conversations**.

They allow:

* training in real working scenarios;
* correcting actual assistant responses;
* adapting the assistant to company-specific processes.

The process is straightforward:

1. You have a conversation with AI Assistant;
2. You correct one of its responses;
3. You select **Train AI** on the AI message;
4. You confirm the training action.

📸 *Screenshot: Train AI option on an AI message*

---

### Important: Training Conversations vs Q&A

⚠️ **Important limitation**

* AI Assistant does **NOT** support Q&A-based training;
* Q&A training is supported **only for Arbiter (Arbitration) models**;
* If a model contains Q&A data, **AI Assistant cannot be built** using that model.

This is not a bug but an intentional architectural decision.

AI Assistant relies on:

* runtime context;
* Training Conversations;
* system instructions.

Arbiter models, on the other hand, are designed for:

* policies and rules;
* static knowledge;
* Q&A-based reasoning.

---

## Models and configuration

Each user in ERP.net has a **Model** setting in their user definition.

This setting determines which AI model is used by AI Assistant.

Important notes:

* the AI Assistant model **cannot be fine-tuned**;
* fine-tuning is supported **only for Arbiter models**.

---

## Debugging and support tools

AI Assistant provides diagnostic tools intended primarily for support and development teams.

### Debug Mode

When enabled:

* diagnostic information is added to each AI response;
* token usage and technical details are displayed.

### Debug Info

Debug Info provides:

* request and response details;
* information required for investigating issues.

These tools should be used **only when necessary and upon request by the support team**.

---

## Summary

AI Assistant in ERP.net is designed to be practical, contextual, and adaptable.

When used correctly, it:

* saves time;
* reduces manual effort;
* supports users directly within their working process.
