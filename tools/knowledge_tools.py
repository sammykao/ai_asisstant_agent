from langchain_community.tools import BraveSearch
import os

class KnowledgeTools:
    def __init__(self, brave_api_key=None):
        self.brave_api_key = os.getenv("BRAVE_API_KEY")
        if not self.brave_api_key:
            raise ValueError("Brave Search API key is required")
        self.brave_search = BraveSearch.from_api_key(api_key=self.brave_api_key, search_kwargs={"count": 5})

    def get_tools(self):
        return [self.brave_search]
