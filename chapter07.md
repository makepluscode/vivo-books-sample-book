# 7장. 도구를 쓰는 날씨 에이전트

> VIVO BOOKS 데모용 가상 기술서예요. 실제로 출간된 책의 원고나 예제가 아니에요.

<!-- drift:explanation -->
이 예제는 LangChain 0.3 방식이에요. `Tool`로 날씨 도구를 감싸고, `create_react_agent()`로 ReAct 에이전트를 만든 뒤 `AgentExecutor`로 실행해요. `invoke()`에 `question`을 넘기면 결과 딕셔너리의 `output`에 최종 답이 담겨요.
<!-- /drift:explanation -->

```python
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
```

`make_model()`은 외부 LLM을 부르지 않는 테스트용 채팅 모델이고, 날씨 도구는 고정된 값을 돌려줘요. 실제 LangChain 에이전트가 도구를 호출하는 흐름을 확인하기 위한 설정이에요.
예상 출력은 `Seoul: sunny, 22 C`예요. 이 예제는 저장소 루트의 `ch07_weather_agent.py`예요.
