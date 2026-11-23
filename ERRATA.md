# 독자 정오표

## r2 · 2026-11-23

- 1장 5행
  - 이전: 이 책의 예제는 LangChain 0.3.25, langchain-core 0.3.61 환경에서 실행을 확인했어요.
  - 이후: 이 개정판의 실습 기준은 LangChain 1.5.0, langchain-core 1.8.1 환경이에요.
- 1장 10행
  - 이전: pip install langchain==0.3.25 langchain-core==0.3.61
  - 이후: pip install langchain==1.5.0 langchain-core==1.8.1
- 1장 13행
  - 이전: 4장에서는 `langchain.prompts` 모듈의 `ChatPromptTemplate`으로 프롬프트를 만들어요.
  - 이후: 4장에서는 `langchain_core.prompts` 모듈의 `ChatPromptTemplate`으로 프롬프트를 만들어요.
- 1장 15행
  - 이전: 7장에서는 `create_react_agent()`로 ReAct 에이전트를 만들고 `AgentExecutor`로 실행해요.
  - 이후: 7장에서는 `create_agent()`로 에이전트를 만들고 실행해요.
- 4장 예제: LangChain v1(설치 버전 langchain 1.5.0)에서는 langchain 네임스페이스가 축소되어 `langchain.prompts` 모듈이 없어졌기 때문에 원래 코드는 ModuleNotFoundError로 실패해요.
  - 이전: `from langchain.prompts import ChatPromptTemplate`
  - 이후: `from langchain_core.prompts import ChatPromptTemplate`
  - 예제를 설명하는 문단도 새 코드에 맞게 고쳤어요.
- 7장 예제: LangChain 1.x에서는 `langchain.agents`에서 `Tool`을 가져올 수 없어서 원래 예제가 ImportError로 실패해요. 공식 문서에 따르면 1.0에서는 `create_agent`로 에이전트를 만드는 것이 표준 방식이에요.
  - 예제 코드를 새 방식으로 다시 썼어요(삭제 27줄 · 추가 8줄). 전체 코드는 개정판을 확인해 주세요.
  - 이전 import: `from langchain.agents import Tool`
  - 이전 import: `from langchain.agents.agent import AgentExecutor`
  - 이전 import: `from langchain.agents.react.agent import create_react_agent`
  - 이전 import: `from langchain_core.prompts import ChatPromptTemplate`
  - 이후 import: `from langchain.agents import create_agent`
  - 예제를 설명하는 문단도 새 코드에 맞게 고쳤어요.
