from environment import EmailEnv
from tasks import hard_emails
from models import Action

env = EmailEnv(hard_emails)

print("[START]")

obs = env.reset()
total_score = 0

while True:
    if not obs.inbox:
        break

    # ⭐ SELECT BEST EMAIL (IMPORTANT)
    email = max(
        obs.inbox,
        key=lambda e: (
            e.priority == "high",
            e.sentiment == "angry"
        )
    )

    # ⭐ SMART DECISION LOGIC
    if email.priority == "high":
        action_type = "escalate"
    elif "spam" in email.subject.lower():
        action_type = "ignore"
    else:
        action_type = "reply"

    # ⭐ SMART RESPONSE
    if action_type == "reply":
        if email.sentiment in ["angry", "frustrated"]:
            response = "Sorry for the inconvenience. We understand your concern and will resolve it quickly."
        else:
            response = "Thank you for reaching out. We will assist you shortly."
    else:
        response = None

    action = Action(
        email_id=email.id,
        action_type=action_type,
        response=response
    )

    obs, reward, done, info = env.step(action)

    print(f"[STEP] action={action_type} reward={reward}")

    total_score += reward

    if done:
        break

print(f"[END] total_score={round(total_score, 2)}")
