from langgraph.prebuilt import create_react_agent

class ConversationalAgent:
    def __init__(self):
        self.agent = create_react_agent(
            model="anthropic:claude-3-5-sonnet-20240620",
            prompt="You are a conversational agent. You are able to answer questions and help with tasks.",
            tools=[],
            name="conversational_agent"
        )

    def __getattr__(self, name):
        # Delegate all unknown attributes/methods to the internal agent
        return getattr(self.agent, name)

