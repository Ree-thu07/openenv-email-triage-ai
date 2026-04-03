from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    id: str
    subject: str
    body: str
    priority: str = "low"
    sentiment: str = "neutral"

class Observation(BaseModel):
    inbox: List[Email]
    history: List[str] = []

class Action(BaseModel):
    email_id: str
    action_type: str  # reply / ignore / escalate
    response: Optional[str] = None

class Reward(BaseModel):
    score: float
    feedback: str