# 4장. 프롬프트 템플릿으로 날씨 도우미 만들기

> VIVO BOOKS 데모용 가상 기술서예요. 실제로 출간된 책의 원고나 예제가 아니에요.

<!-- drift:explanation -->
`ChatPromptTemplate`은 `langchain_core.prompts`에서 가져와요. LangChain v1부터 `langchain` 패키지는 에이전트에 꼭 필요한 기능 위주로 정리되어 `langchain.prompts` 경로로는 더 이상 가져올 수 없어요. `ChatPromptTemplate.from_template()`은 템플릿 문자열 하나로 사람(human) 메시지 하나짜리 채팅 프롬프트를 만들고, 그 안의 `{question}` 자리에 질문이 들어가요. 프롬프트, 모델, 출력 파서를 `|`로 이어 체인을 만들고 `invoke()`에 `{"question": 질문}` 딕셔너리를 넘기면, 모델이 돌려준 메시지를 `StrOutputParser`가 문자열로 바꿔 줘요. 그래서 `ask()`는 이 문자열을 그대로 반환해요.
<!-- /drift:explanation -->

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vivo_demo import make_chat_model

# 1. 질문이 들어갈 자리가 있는 프롬프트
prompt = ChatPromptTemplate.from_template(
    "당신은 날씨를 쉽게 설명하는 도우미예요. 다음 질문에 짧게 답해 주세요. 질문: {question}"
)

# 2. 테스트용 채팅 모델과 문자열 출력 파서
llm = make_chat_model()
output_parser = StrOutputParser()

# 3. 프롬프트 → 모델 → 출력 파서를 하나의 체인으로
chain = prompt | llm | output_parser


def ask(question):
    return chain.invoke({"question": question})


print(ask("서울 날씨는?"))
```

`make_chat_model()`은 받은 프롬프트를 그대로 되돌려 주는 테스트용 채팅 모델이에요. 출력에 프롬프트 문장이 보이면 템플릿이 제대로 적용된 거예요. 이 예제는 저장소의 `examples/ch04_prompt_template.py`예요.
