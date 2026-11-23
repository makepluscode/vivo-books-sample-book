from langchain.agents import Tool
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from vivo_demo import make_model, weather

# 1. ReAct 형식 프롬프트: 생각 → 도구 호출 → 관찰 → 최종 답
prompt = ChatPromptTemplate.from_template(
    """당신은 날씨 질문에 답하는 도우미예요. 필요하면 다음 도구를 쓸 수 있어요:
{tools}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {question}
Thought:{agent_scratchpad}"""
)


def answer_city(city):
    # 2. 테스트용 모델과 날씨 도구
    llm = make_model(city)
    weather_tool = Tool(name="weather", func=weather.run,
                        description="도시 이름을 받아 현재 날씨를 알려 주는 도구")
    tools = [weather_tool]

    # 3. 에이전트와 실행기
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)

    # 4. 실행하고 최종 답 꺼내기
    result = agent_executor.invoke({"question": city})
    return result["output"]


print(answer_city("Seoul"))
