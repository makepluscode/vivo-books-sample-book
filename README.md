# 날씨 도우미로 배우는 LangChain 첫걸음 (가상 기술서)

VIVO BOOKS — 살아 있는 기술서(제1회 라이너 해커톤 출품작) 데모를 위해 만든 **가상의 기술서**예요. 실제로 출간된 책의 원고나 예제가 아니에요.

원고는 LangChain 0.3.25 기준으로 썼어요(r1). LangChain에 새 버전이 나오면 VIVO BOOKS 감시기가 예제를 최신 환경에서 실행해 보고, Liner로 공식 문서 근거를 찾아 코드와 설명을 고친 개정안을 **Pull Request**로 제안해요. 저자는 PR에서 바뀐 원고·예제 파일·정오표·개정 EPUB을 검토하고 병합 여부를 정해요.

## 구성

| 파일 | 내용 |
|---|---|
| `chapter01.md` | 1장 실습 환경 준비하기 — 버전 표기, 설치 명령, 장별 안내 |
| `chapter03.md` | 3장 로컬 모델 이름 정하기 — LangChain을 쓰지 않는 장(영향 없음) |
| `chapter04.md` · `ch04_prompt_template.py` | 4장 프롬프트 템플릿으로 날씨 도우미 만들기 |
| `chapter07.md` · `ch07_weather_agent.py` | 7장 도구를 쓰는 날씨 에이전트 |
| `vivo_demo.py` | 외부 LLM·날씨 API 없이 예제를 돌리는 테스트용 채팅 모델과 날씨 도구 |
| `book.json` | VIVO BOOKS 설정 — 고정 버전, 감시할 패키지, 장별 검증 계약 |
| `requirements.txt` | 원고 기준 고정 버전 |

## 예제 실행

원고 기준(LangChain 0.3.25)은 Python 3.12에서 확인했어요. Python 3.14에서는 일부 하위 의존성을 소스에서 빌드하다 설치가 실패할 수 있어요.

```bash
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python ch04_prompt_template.py   # 도우미 답변 ← 당신은 날씨를 쉽게 설명하는 도우미예요. …
.venv/bin/python ch07_weather_agent.py     # Seoul: sunny, 22 C
```

최신 LangChain(1.x)을 설치하면 4장은 `ModuleNotFoundError: No module named 'langchain.prompts'`, 7장은 `ImportError: cannot import name 'Tool' from 'langchain.agents'`로 멈춰요. 이 저장소의 Pull Request에서 VIVO BOOKS가 제안한 개정안을 볼 수 있어요.

## 라이선스

[MIT](LICENSE)
