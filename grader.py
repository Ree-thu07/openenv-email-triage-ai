def grade(email, action):
    score = 0.0
    feedback = ""

    # Action correctness
    if action.action_type == email["expected_action"]:
        score += 0.5
        feedback += "Correct action. "
    else:
        score -= 0.3
        feedback += "Wrong action. "

    # Response quality
    if action.action_type == "reply":
        if action.response:
            words = action.response.split()

            if len(words) > 5:
                score += 0.2
                feedback += "Detailed response. "

            if any(w in action.response.lower() for w in ["thank", "sorry"]):
                score += 0.2
                feedback += "Polite tone. "

            if "help" in action.response.lower():
                score += 0.1
                feedback += "Helpful intent. "

        else:
            score -= 0.2
            feedback += "Empty response. "

    # Penalize unnecessary escalation
    if action.action_type == "escalate" and email["expected_action"] != "escalate":
        score -= 0.2
        feedback += "Unnecessary escalation. "

    return max(score, 0.0), feedback