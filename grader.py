def grade(email, action):
    score = 0.0
    feedback = ""

    # 1. Ground truth (basic correctness)
    if "expected_action" in email:
        if action.action_type == email["expected_action"]:
            score += 0.4
            feedback += "Correct action. "
        else:
            score -= 0.3
            feedback += "Wrong action. "

    # 2. Real-world logic (IMPORTANT)
    if email.get("priority") == "high" and action.action_type == "escalate":
        score += 0.2
        feedback += "Handled urgency well. "

    # 3. Apology check
    if email.get("requires_apology"):
        if action.response and "sorry" in action.response.lower():
            score += 0.2
            feedback += "Proper apology. "
        else:
            score -= 0.2
            feedback += "Missing apology. "

    # 4. Response quality
    if action.response:
        if len(action.response.split()) > 5:
            score += 0.1
            feedback += "Detailed response. "

        if any(w in action.response.lower() for w in ["thank", "sorry"]):
            score += 0.1
            feedback += "Polite tone. "

    # 5. Penalize bad escalation
    if action.action_type == "escalate" and email.get("priority") != "high":
        score -= 0.2
        feedback += "Unnecessary escalation. "

    # Clamp score
    score = max(0.0, min(1.0, score))

    return score, feedback
