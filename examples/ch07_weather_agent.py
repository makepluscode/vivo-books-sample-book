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
