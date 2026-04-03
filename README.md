# Email Triage OpenEnv

## Description
This environment simulates real-world email triage tasks where an AI agent must classify and respond to emails.

## Tasks
- Easy: Basic classification
- Medium: Classification + response
- Hard: Escalation + reasoning

## Action Space
- reply
- ignore
- escalate

## Observation Space
- Inbox emails
- History

## Reward
- Correct action: +0.5
- Good response: +0.3
- Politeness: +0.2
- Wrong action: -0.3

## Run

```bash
docker build -t email-env .
docker run email-env