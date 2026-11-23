# 1장. 실습 환경 준비하기

> VIVO BOOKS 데모용 가상 기술서예요. 실제로 출간된 책의 원고나 예제가 아니에요.

이 개정판의 실습 기준은 LangChain 1.5.0, langchain-core 1.8.1 환경이에요.

다음 명령으로 실습에 필요한 패키지를 설치해요.

```bash
pip install langchain==1.5.0 langchain-core==1.8.1
```

4장에서는 `langchain_core.prompts` 모듈의 `ChatPromptTemplate`으로 프롬프트를 만들어요.

7장에서는 `create_agent()`로 에이전트를 만들고 실행한 뒤, 결과를 메시지 목록에서 꺼내요.

각 장의 예제는 `make_model()` 같은 테스트용 모델을 써서 API 키 없이 실행할 수 있어요.

예제 파일은 저장소 `github.com/makepluscode/vivo-books-sample-book`의 `examples/` 폴더에 있어요. 저장소 루트에서 `python examples/ch04_prompt_template.py`처럼 장별 파일을 실행하고, 테스트용 모델은 같은 폴더의 `vivo_demo.py`가 제공해요.
