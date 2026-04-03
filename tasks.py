# EASY TASK
easy_emails = [
    {
        "id": "1",
        "subject": "Application status",
        "body": "Can you update me?",
        "expected_action": "reply"
    },
    {
        "id": "2",
        "subject": "Win money now!!!",
        "body": "Click here",
        "expected_action": "ignore"
    }
]

# MEDIUM TASK
medium_emails = [
    {
        "id": "3",
        "subject": "Refund request",
        "body": "I want a refund for my purchase",
        "expected_action": "reply"
    },
    {
        "id": "4",
        "subject": "Account hacked",
        "body": "Someone accessed my account!",
        "expected_action": "escalate",
        "priority": "high",
        "sentiment": "angry"
    }
]

# HARD TASK
hard_emails = [
    {
        "id": "H1",
        "subject": "Legal escalation: data breach",
        "body": "We may take legal action if not resolved immediately.",
        "priority": "high",
        "sentiment": "angry",
        "requires_apology": True,
        "requires_escalation": True
    },
    {
        "id": "H2",
        "subject": "Service outage affecting business",
        "body": "Our operations are down. Need urgent fix.",
        "priority": "high",
        "sentiment": "frustrated",
        "requires_escalation": True
    }
]
