def summary_agent(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:3])
    return f"Executive Overview:\n{summary.strip()}"


def risk_agent(text):
    risks = []
    for line in text.split("."):
        if any(word in line.lower() for word in ["risk", "delay", "issue", "concern", "challenge"]):
            risks.append(line.strip())
    return risks[:5]


def strategy_agent(text):
    strategies = []
    for line in text.split("."):
        if any(word in line.lower() for word in ["plan", "improve", "increase", "optimize", "expand"]):
            strategies.append(line.strip())
    return strategies[:5]