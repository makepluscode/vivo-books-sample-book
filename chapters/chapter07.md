# 7장. 도구를 쓰는 날씨 에이전트

> VIVO BOOKS 데모용 가상 기술서예요. 실제로 출간된 책의 원고나 예제가 아니에요.

<!-- drift:explanation -->
이 예제는 LangChain 1.x 방식이에요. 0.3의 `create_react_agent()`와 `AgentExecutor` 조합 대신 `create_agent()` 하나로 에이전트를 만들어요. `tools`에는 `BaseTool` 인스턴스를 그대로 넘길 수 있어서 `weather` 도구를 `Tool`로 다시 감싸지 않고 리스트에 바로 넣어요. ReAct 형식 프롬프트 템플릿은 더 이상 필요 없고, 에이전트의 역할만 `system_prompt` 문자열로 알려 줘요. 입력도 달라졌어요. `invoke()`에는 `{"messages": [{"role": "user", "content": city}]}`처럼 메시지 목록을 넘겨요. 반환값은 `messages` 목록을 담은 상태 딕셔너리이고, 최종 답은 이 목록의 마지막 AI 메시지인 `result["messages"][-1].content`에서 꺼내요.
<!-- /drift:explanation -->

```python
from langchain.agents import create_agent
from vivo_demo import make_model, weather

# 1. 시스템 프롬프트: ReAct 형식 템플릿 대신 에이전트의 역할만 알려 줘요
SYSTEM_PROMPT = "당신은 날씨 질문에 답하는 도우미예요. 필요하면 weather 도구를 써서 답하세요."


def answer_city(city):
    # 2. 테스트용 모델과 날씨 도구
    llm = make_model(city)
    tools = [weather]

    # 3. 에이전트 만들기 (별도의 실행기가 필요 없어요)
    agent = create_agent(llm, tools=tools, system_prompt=SYSTEM_PROMPT)

    # 4. 실행하고 최종 답 꺼내기
    result = agent.invoke({"messages": [{"role": "user", "content": city}]})
    return result["messages"][-1].content


print(answer_city("Seoul"))
```

`make_model()`은 외부 LLM을 부르지 않는 테스트용 채팅 모델이고, 날씨 도구는 고정된 값을 돌려줘요. 실제 LangChain 에이전트가 도구를 호출하는 흐름을 확인하기 위한 설정이에요.
예상 출력은 `Seoul: sunny, 22 C`예요. 이 예제는 저장소의 `examples/ch07_weather_agent.py`예요.
