# 날씨 도우미로 배우는 LangChain 첫걸음 (가상 기술서)

[VIVO BOOKS — 살아 있는 기술서](https://github.com/makepluscode/vivo-books-agent)(제1회 라이너 해커톤 출품작)가 감시하는 **데모용 가상 기술서**예요. 실제로 출간된 책의 원고나 예제가 아니에요.

LangChain에 새 버전이 나오면 VIVO BOOKS가 이 책의 예제를 최신 환경에서 실행해 보고, Liner로 공식 문서 근거를 찾아 원고와 예제를 고친 개정판을 **Pull Request**로 보내요. 저자는 PR에서 바뀐 원고, 예제 파일, 독자 정오표, 개정 EPUB을 검토하고 병합할지 정해요.

- 첫 원고(r1, LangChain 0.3.25): 이 저장소의 `main`
- VIVO BOOKS의 개정 제안(r2, LangChain 1.5.0): [Pull Requests](https://github.com/makepluscode/vivo-books-sample-book/pulls)

## 구조

```text
.
├── README.md                이 안내
├── book.json                VIVO BOOKS 설정: 판본, 고정 버전, 감시할 패키지, 장별 검증 방법
├── requirements.txt         예제의 실행 기준 버전
├── chapters/                원고
│   ├── chapter01.md         1장 실습 환경 준비하기 (버전 표기, 설치 명령, 장별 안내)
│   ├── chapter03.md         3장 로컬 모델 이름 정하기 (LangChain을 쓰지 않는 대조군)
│   ├── chapter04.md         4장 프롬프트 템플릿으로 날씨 도우미 만들기
│   └── chapter07.md         7장 도구를 쓰는 날씨 에이전트
├── examples/                원고 속 예제 코드
│   ├── ch04_prompt_template.py
│   ├── ch07_weather_agent.py
│   └── vivo_demo.py         외부 LLM·날씨 API 없이 예제를 돌리는 테스트용 모델과 날씨 도구
├── LICENSE                  MIT
└── THIRD_PARTY_NOTICES.md   LangChain에서 가져온 ReAct 형식 프롬프트의 고지
```

## 예제 실행

`requirements.txt`대로 설치하면 그 판본의 예제가 실행돼요. r1(LangChain 0.3.25)은 Python 3.12에서 확인했어요. Python 3.14에 0.3.25를 설치하면 일부 하위 의존성을 소스에서 빌드하다 실패할 수 있어요.

```bash
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python examples/ch04_prompt_template.py   # 도우미 답변 ← 당신은 날씨를 쉽게 설명하는 도우미예요. …
.venv/bin/python examples/ch07_weather_agent.py     # Seoul: sunny, 22 C
```

r1 예제를 최신 LangChain(1.x)에서 실행하면 4장은 `ModuleNotFoundError: No module named 'langchain.prompts'`, 7장은 `ImportError: cannot import name 'Tool' from 'langchain.agents'`로 멈춰요. 개정 PR 브랜치의 `requirements.txt`(LangChain 1.5.0)대로 설치하면 예제가 다시 실행돼요.

## 라이선스

[MIT](LICENSE). 7장 r1 예제의 ReAct 형식 프롬프트는 LangChain(MIT)의 예시를 따랐어요. 원 저작권 고지는 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)에 있어요.
