"""테스트용 채팅 모델과 날씨 도구 — 외부 LLM·날씨 API 없이 예제를 실행해요.

- make_model(city): 날씨 도구를 한 번 부른 뒤 도구 결과로 답하는 채팅 모델.
  LangChain 0.3의 ReAct 텍스트 방식과 1.x의 도구 호출(tool call) 방식 모두에서 동작해요.
- weather: 도시 이름을 받아 고정된 날씨를 돌려주는 도구.
- make_chat_model(): 받은 프롬프트를 그대로 되돌려 주는 채팅 모델(프롬프트 템플릿 확인용).
"""
from langchain_core.language_models.fake_chat_models import FakeMessagesListChatModel
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.tools import tool

weather_calls = []
model_inputs = []


def _weather_control():
    suffix = ""

    def value():
        return suffix

    def set_suffix(new_value):
        nonlocal suffix
        suffix = new_value

    return value, set_suffix


_weather_suffix, _set_weather_suffix = _weather_control()


class LocalChatModel(FakeMessagesListChatModel):
    def bind_tools(self, tools, **kwargs):
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        model_inputs.append([{"type": m.type, "content": m.content,
                              "name": m.name, "tool_call_id": getattr(m, "tool_call_id", None)}
                             for m in messages])
        # 도구 호출 방식: LangChain이 전달한 도구 결과(ToolMessage)를 그대로 최종 답으로 써요.
        if isinstance(messages[-1], ToolMessage):
            return ChatResult(generations=[ChatGeneration(
                message=AIMessage(content=str(messages[-1].content)))])
        return super()._generate(messages, stop, run_manager, **kwargs)


@tool
def weather(city: str) -> str:
    """Return a fixed weather fixture for a city, with no network access."""
    weather_calls.append(city)
    return f"{city}: sunny, 22 C{_weather_suffix()}"


def make_model(city):
    return LocalChatModel(responses=[
        # 첫 응답: 날씨 도구를 부르라는 요청(ReAct 텍스트와 tool call을 함께 담아요)
        AIMessage(
            content=f"Action: weather\nAction Input: {city}",
            tool_calls=[{"name": "weather", "args": {"city": city},
                         "id": "weather-1", "type": "tool_call"}],
        ),
        # ReAct 텍스트 방식의 두 번째 응답(0.3의 AgentExecutor가 읽는 형식)
        AIMessage(content=f"Final Answer: {city}: sunny, 22 C"),
    ])


class EchoChatModel(FakeMessagesListChatModel):
    """Answers with the prompt text it received, so the output proves the template was applied."""

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        text = " / ".join(str(m.content) for m in messages)
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content="도우미 답변 ← " + text))])


def make_chat_model():
    return EchoChatModel(responses=[AIMessage(content="")])
