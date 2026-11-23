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
