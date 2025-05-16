from langgraph.prebuilt import create_react_agent
from tools.knowledge_tools import KnowledgeTools


class KnowledgeAgent:
    def __init__(self):
        # Get tools from tools module
        tools = KnowledgeTools().get_tools()
        # init agent
        self.agent = create_react_agent(
            model="anthropic:claude-3-5-sonnet-20240620",
            prompt="You are a knowledge agent. You are able to answer questions and help with tasks.",
            tools=tools,
            name="knowledge_agent"
        )
    
    def __getattr__(self, name):
        # Delegate all unknown attributes/methods to the internal agent
        return getattr(self.agent, name)


