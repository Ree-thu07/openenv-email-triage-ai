from models import Observation, Action, Email
from grader import grade
from tasks import easy_emails

class EmailEnv:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0
        self.history = []

    def reset(self):
        self.index = 0
        self.history = []
        return self.state()

    def state(self):
        if self.index >= len(self.emails):
            return Observation(inbox=[], history=self.history)

        batch = self.emails[self.index:self.index+2]

        return Observation(
        inbox=[Email(**e) for e in batch],
        history=self.history
    )

    def step(self, action: Action):
        email = self.emails[self.index]

        reward, feedback = grade(email, action)

        self.history.append(f"{action.action_type} on {email['id']}")
        self.index += 1

        if len(self.history) > 15:
            return self.state(), 0.0, True, {"feedback": "Loop detected"}

        done = self.index >= len(self.emails)

        return self.state(), reward, done, {"feedback": feedback}