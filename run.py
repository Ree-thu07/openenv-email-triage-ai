from environment import EmailEnv
from models import Action
from tasks import easy_emails

env = EmailEnv(easy_emails)

obs = env.reset()

while True:
    if not obs.inbox:
        break

    email = obs.inbox[0]
    print("Email:", email.subject)

    action = Action(
        email_id=email.id,
        action_type="reply",
        response="Thank you, we will help you soon."
    )

    obs, reward, done, info = env.step(action)

    print("Reward:", reward, "| Feedback:", info["feedback"])

    if done:
        break