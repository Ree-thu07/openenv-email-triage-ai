from environment import EmailEnv
from tasks import hard_emails
from models import Action

# Initialize env
env = EmailEnv(hard_emails)

print("[START]")

obs = env.reset()
total_score = 0

step_count = 0

while True:
    if not obs.inbox:
        break

    email = obs.inbox[0]

    # Simple baseline logic
    if "urgent" in email.subject.lower() or email.priority == "high":
        action_type = "escalate"
    elif "spam" in email.subject.lower():
        action_type = "ignore"
    else:
        action_type = "reply"

    action = Action(
        email_id=email.id,
        action_type=action_type,
        response="Thank you. We will resolve your issue."
    )

    obs, reward, done, info = env.step(action)

    print(f"[STEP] action={action_type} reward={reward}")

    total_score += reward
    step_count += 1

    if done:
        break

print(f"[END] total_score={round(total_score,2)}")
