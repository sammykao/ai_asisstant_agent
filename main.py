from langchain_anthropic import ChatAnthropic
from langgraph_supervisor import create_supervisor
from agents.conversational_agent import ConversationalAgent
from agents.knowledge_agent import KnowledgeAgent
from dotenv import load_dotenv
import os

load_dotenv()
ChatAnthropic.api_key = os.getenv("ANTHROPIC_API_KEY")


class AgentManager:
    def __init__(self):
        self.conversational_agent = ConversationalAgent()
        self.knowledge_agent = KnowledgeAgent()

        self.supervisor = create_supervisor(
            agents=[self.conversational_agent, self.knowledge_agent],
            model=ChatAnthropic("claude-3-5-sonnet-20240620"),
            prompt=(
                "You manage a conversation agent, and a knowledge agent."
                "Assign work to them based on the user's request."
            )
        ).compile()

    def run(self, user_input: str):
        return self.supervisor.invoke({"messages": [{"role": "user", "content": user_input}]})


if __name__ == "__main__":
    print("Starting agent manager...")
    agent_manager = AgentManager()
    print("Running agent manager...")
    print(agent_manager.run("What is the capital of France?"))
