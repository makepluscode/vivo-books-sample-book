# 개정 이력

## r2 미리보기 · 2026-11-23

감지: langchain 0.3.25 → 1.5.2, langchain-core 0.3.61 → 1.8.4 · 검증 환경: langchain==1.5.0, langchain-core==1.8.1

| 장 | 문제 | 수정 | 근거 | 검증 |
|---|---|---|---|---|
| 1장 | 고정 버전 표기·옛 API 설명 | 버전 표기 2곳 동기화 · 본문 문장 2곳 | [LangChain v1 migration guide](https://docs.langchain.com/oss/python/migrate/langchain-v1) “The langchain package namespace has been significantly”<br>[What's new in LangChain v1 - Docs by…](https://docs.langchain.com/oss/python/releases/langchain-v1) “create_agent is the standard way to build agents in LangChain 1.0.…” | 설치 가능 확인(pip dry-run) |
| 3장 | 의존성 없음 | 유지 | — | — |
| 4장 | `ModuleNotFoundError: No module named 'langchain.prompts'` | 코드·설명 문단 | [What's new in LangChain v1](https://docs.langchain.com/oss/python/releases/langchain-v1) “The langchain namespace has been streamlined to focus on essential…”<br>[prompts \| langchain_core](https://reference.langchain.com/python/langchain-core/prompts) “from langchain_core.prompts import ChatPromptTemplate” | prompt \| 테스트 채팅 모델 \| 출력 파서 체인 경유 + 숨은 질문의 기대 출력 일치 |
| 7장 | `ImportError: cannot import name 'Tool' from 'langchain.agents'` | 코드·설명 문단 | [What's new in LangChain v1](https://docs.langchain.com/oss/python/releases/langchain-v1) “create_agent is the standard way to build agents in LangChain 1.0.”<br>[LangChain v1 migration guide](https://docs.langchain.com/oss/python/migrate/langchain-v1) “The tools argument to create_agent accepts a list of: LangChain…” | Seoul·Busan·Jeju 실행 + 도구 응답 변경 확인 + 처음 보는 도시의 최종 AI 답 확인 · 테스트 모델·고정 날씨 도구 |
