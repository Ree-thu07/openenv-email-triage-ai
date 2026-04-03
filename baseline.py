import os
from openai import OpenAI # type: ignore
from environment import EmailEnv
from models import Action
from tasks import hard_emails

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

env = EmailEnv(hard_emails)
obs = env.reset()
total_score = 0

while True:
    if not obs.inbox:
        break

    email = obs.inbox[0]

    prompt = f"""
    You are a professional email assistant.

    Email:
    Subject: {email.subject}
    Body: {email.body}

    Rules:
    - Spam → ignore
    - Complaint → reply politely
    - Serious/legal → escalate
    - Always be professional

    Output ONLY in this format:
    action: <reply/ignore/escalate>
    response: <text or none>
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.lower()

    if "ignore" in text:
        action_type = "ignore"
    elif "escalate" in text:
        action_type = "escalate"
    else:
        action_type = "reply"

    action = Action(
        email_id=email.id,
        action_type=action_type,
        response="Thank you for reaching out. We will assist you shortly."
    )

    obs, reward, done, _ = env.step(action)
    total_score += reward

    if done:
        break

print("Improved Baseline Score:", total_score)