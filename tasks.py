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
        "expected_action": "escalate"
        "priority": "high",
        "sentiment": "angry"
    }
]

# HARD TASK
hard_emails = [
    {
        "id": "5",
        "subject": "Legal complaint",
        "body": "I will file a complaint if not resolved",
        "expected_action": "escalate"
    },
    {
        "id": "6",
        "subject": "Product feedback",
        "body": "Loved your product but needs improvements",
        "expected_action": "reply"
    }
]