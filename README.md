# 📧 OpenEnv Email Triage AI Environment

## 🚀 Overview

This project implements a **real-world AI environment** where an agent learns to classify, prioritize, and respond to customer emails using a structured `step() / reset() / state()` interface.

The environment simulates **customer support workflows**, enabling evaluation of intelligent agents in realistic scenarios.

---

## 🎯 Features

* OpenEnv-compatible API design
* Typed Pydantic models (Observation, Action, Reward)
* Multi-level tasks (easy → medium → hard)
* Priority & sentiment-aware decision making
* Reward shaping with partial scoring
* Hugging Face model integration (OpenAI client format)
* FastAPI interface for interaction
* Dockerized deployment

---

## 🧠 Problem Statement

In real-world customer support systems, AI agents must:

* Understand incoming emails
* Determine the correct action
* Generate professional responses

This environment provides a structured way to train and evaluate such agents.

---

## 📊 Action Space

* **reply** → respond to email
* **ignore** → discard spam or irrelevant email
* **escalate** → forward critical or urgent issues

---

## 👀 Observation Space

* Inbox (list of emails)
* Interaction history

---

## 🧪 Tasks

### 🟢 Easy

Basic classification (spam vs normal)

### 🟡 Medium

Complaint handling with tone awareness

### 🔴 Hard

Complex reasoning involving urgency, escalation, and apology handling

---

## 🎯 Reward Design

The environment provides continuous feedback through a shaped reward function:

* Correct action → +0.5
* Detailed response → +0.2
* Polite tone (e.g., "thank you", "sorry") → +0.2
* Wrong action → -0.3
* Missing required apology → penalty

All rewards are clamped between **0.0 and 1.0** to ensure consistency.

---

## ⚙️ Run Locally

```bash
python -m pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 🐳 Docker

```bash
docker build -t email-env .
docker run email-env
```

---

## 🤗 Deployment

This project is deployed using **Hugging Face Spaces (Docker SDK)**.
The application runs on port **7860** and exposes API endpoints for interaction.

---

## 📌 Author

**Reethu S**
