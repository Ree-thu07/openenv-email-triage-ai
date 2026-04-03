from fastapi import FastAPI  
from environment import EmailEnv
from tasks import hard_emails
from models import Action

app = FastAPI()

env = EmailEnv(hard_emails)


# ✅ RESET endpoint
@app.get("/reset")
def reset():
    obs = env.reset()
    return {
        "state": {
            "inbox": [e.model_dump() for e in obs.inbox],
            "history": obs.history
        }
    }


# ✅ HOME endpoint
@app.get("/")
def home():
    obs = env.reset()

    if not obs.inbox:
        return {"message": "No emails available"}

    return {
        "message": "Email Triage Environment",
        "email": obs.inbox[0].model_dump()
    }


# ✅ STEP endpoint
@app.post("/step")
def step(action: dict):
    try:
        action_obj = Action(**action)
    except Exception as e:
        return {"error": str(e)}

    obs, reward, done, info = env.step(action_obj)

    return {
        "next_state": {
            "inbox": [e.model_dump() for e in obs.inbox],
            "history": obs.history
        },
        "reward": reward,
        "done": done,
        "feedback": info
    }
