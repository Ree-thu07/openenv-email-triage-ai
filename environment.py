from models import Observation, Action, Email
from grader import grade


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
        # End condition (VERY IMPORTANT)
        if self.index >= len(self.emails):
            return Observation(inbox=[], history=self.history)

        # Multi-email batch
        batch = self.emails[self.index:self.index + 2]

        return Observation(
            inbox=[Email(**e) for e in batch],
            history=self.history
        )

    def step(self, action: Action):
        # Safety check (avoid crash)
        if self.index >= len(self.emails):
            return self.state(), 0.0, True, {"feedback": "No more emails"}

        email = next((e for e in self.emails if e["id"] == action.email_id), None)

        if email.get("priority") == "high" and action.action_type == "ignore":
            reward -= 0.4
        if not email:
            return self.state(), 0.0, False, {"feedback": "Invalid email_id"}

        reward, feedback = grade(email, action)

        # Track history
        action_record = f"{action.action_type}:{email['id']}"
        self.history.append(action_record)

        # Loop penalty (if same action repeated)
        if self.history.count(action_record) > 1:
            reward -= 0.2

        # Apology reward (real-world behavior)
        if action.response and "sorry" in action.response.lower():
            reward += 0.2

        # Move to next email
        self.index += 1

        # Loop termination
        if len(self.history) > 15:
            return self.state(), 0.0, True, {"feedback": "Loop detected"}

        # Episode done condition
        done = self.index >= len(self.emails)

        # Clamp reward (MANDATORY for submission)
        reward = max(0.0, min(1.0, reward))

        return self.state(), reward, done, {"feedback": feedback}
