from langchain.agents import create_agent
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # 실행 위치와 무관하게 프로젝트 루트 추가
from common_config import llm_connect

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


model =llm_connect()

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
)

print(result) 
