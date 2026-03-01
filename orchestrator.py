from agents import summary_agent, risk_agent, strategy_agent


def route_to_agents(text):
    summary = summary_agent(text)
    risks = risk_agent(text)
    strategies = strategy_agent(text)

    return {
        "summary": summary,
        "risks": risks,
        "strategies": strategies
    }


def generate_executive_brief(text):
    return route_to_agents(text)

   