import os
import json
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv("./.gitignore/.env")

print("\n----Input-----")
query = str(input())

tavily_api_key = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=tavily_api_key)
search_result = client.get_search_context(
    query=query,
    max_results=1
)

if isinstance(search_result, str):
    search_result = json.loads(search_result)

result = search_result[0]
print(json.dumps(result["content"], ensure_ascii=False))