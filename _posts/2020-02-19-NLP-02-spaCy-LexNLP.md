---
title: "NLP - 02 spaCy & LexNLP"
date: 2020-02-19
categories: NLP
---

## 1. Intro

앞서 언급했듯 NLTK의 경우 각 함수가 string을 입력받아 그 결과물로 string을 반환하여 직관적으로 그 구조를 이해하기 어렵지 않으나, spaCy의 경우 자체 object를 반환하기에 그 구조를 간단히 살펴볼 필요가 있다. 따라서 본 글에서는 spaCy를 활용하기 이전에 그 구조를 간단히 살펴보고자 한다. 또한 앞서 소개되지는 않았고 인지도도 그렇게 크지는 않지만, Edgar을 통해 훈련됐다고 주장하는 NLP 라이브러리인 LexNLP에 대해 간략히 살펴보도록 한다.

## 2. spaCy

함수의 입력으로 string을 받는 NLTK와 달리 spaCy는 자체적인 Container을 그 입력으로 받는다. Container에는 `Doc`, `Token`, `Span`, `Lexeme` 네 가지가  있다. 

![img1](https://spacy.io/architecture-bcdfffe5c0b9f221a2f6607f96ca0e4a.svg)

이 중 중심이 되는 것은 string으로 이뤄진 문서를 객체화하는 `Doc`이다. [설명 문서](https://spacy.io/api)에 따르면 `Doc`은 문서를 나름의 pipeline을 통해 재구성하여 저장하는 공간이고, `Token`과 `Span`은 그 문서를 설명하는 두 가지 방식이다. `Token`은 문장이나 단어 등 문서를 이루는 의미 단위로 문서를 설명하는 방식이며, `Span`은 우리가 다른 자료형에서 해왔던 것과 비슷한, 숫자를 이용한 인덱싱방식이다. 이 외 `Vocab`과 `Lexeme`은 단어를 인코딩하는 방식인데, 본 지면의 목적과 다르므로 이후 필요하면 서술하기로 한다. 우리가 다루고자 하는 task에서 기억해야 할 건, 우리가 주로 사용할 함수는 주로 `Doc` 객체 수준에서 다뤄진다는 점이다. 그렇다면 `Doc` 객체는 어떻게 만들어지는가?

![img2](https://spacy.io/pipeline-7a14d4edd18f3edfee8f34393bff2992.svg)

일차적으로 spaCy는 문서 그 자체를 있는 그대로 `Doc`으로 만들어주는, 따라서 tokenization 등(이러한 전처리 과정을 spaCy는 `pipeline`이라 칭한다)이 아직 실행되지 않은 `English` 클래스를 가진다. 그리고 `en_core_web_sm`처럼 spaCy가 나름대로 제작하여 배포하고 있는  [언어 모델](https://spacy.io/models)이 있다. 이를 불러와서 문서를 `Doc`로 만드는 코드는 다음과 같다.

```python
from spacy.lang.en import English

example = 'This is a sentence.'
nlp = English()     # Doc을 만들기 위한 pipeline 불러오기
doc = nlp(example)   # 실행
```

이런 방식으로 `Doc` 객체를 만들고, 이후에 여러 함수를 적용할 수 있다. 물론 `pipeline`이라는 이름이 암시하듯이 여러 전처리 과정을 `nlp`에 추가할 수도 있으며 spaCy의 API 소개란은 두 가지 방식을 모두 다루고 있다.

앞서 언급했듯이 `English` 클래스는 원래의 문서를 그대로 입력으로 받기에 이를 통해 자기 자신만의 `pipeline`을 제작할 수 있으며, tokenization같은 아주 기초적인 전처리 과정이 아니라 NER, POS tagging 등 이차적인 작업을 수행하는 데 목적이 있다면 `en_core_web_sm` 같은 자체 모델을 불러오는 것도 나쁘지 않다. (각 모델의 소개와 성능 비교는 [다음 링크](https://spacy.io/models/en). 아쉽게도 한국어는 지원하지 않는다.)

## 3. [LexNLP](https://arxiv.org/pdf/1806.03688.pdf)

LexNLP는 많이 알려지진 않아 글에 포함시키는 것이 맞을까 고민했으나, Edgar의 데이터로 pre-trained된 모델을 제공한다는 점때문에 포함시키기로 했다. 본 라이브러리는 위 논문의 제목이 말하듯 '*legal and regulatory texts*'를 대상으로 NLP와 IE를 제공한다. 역시 본 글이 주목하는 부분은 IE 부분인데, LexNLP는 주소, 날짜, 금액, named entity 외 여러 정보를 추출할 수 있다(고 한다). 필자가 보기에 LexNLP의 사용에는 다음과 같은 주의점이 따른다.

- 아직 충분히 검증되지 않았다는 점.
- 여전히 오픈소스이긴 하지만 비영리, 영리 이용이 가능하다고 소개된 논문이 쓰인 2년 전과는 달리, [여러 지불 옵션](https://contraxsuite.com/lexnlp-support/)이 홈페이지에서 소개되고 있기에 이용에 확인이 필요하다는 점.
- 본 글이 쓰인 시점을 기준으로 최근 두 달 간의 [github commit](https://github.com/LexPredict/lexpredict-lexnlp/graphs/contributors?from=2017-10-29&to=2020-02-22&type=c) 정보가 없다는 점.

[다음 페이지](https://contraxsuite.com/lexnlp-features/)의 맨 아래 부분을 통해 LexNLP의 IE를 간단하게 실습해볼 수 있다. 한 문단을 통해 실습한 결과 다음과 같은 결과물을 얻었다. (이미는 결과물의 일부)

- (원문) *On August 27, 2018, in connection with the consummation of the Merger, Cotiviti Corporation, a Delaware corporation (“Cotiviti Corporation”), and Cotiviti Domestic Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, the “Borrowers”), each a subsidiary of Cotiviti, repaid in full all outstanding loans, together with interest and all other amounts due in connection with such repayment, under that certain Amended and Restated First Lien Credit Agreement, dated as of September 28, 2016, by and among the Borrowers, Cotiviti Intermediate Holdings, Inc., a Delaware corporation, the lenders party thereto, and JPMorgan Chase Bank, N.A. as administrative agent for the lenders party thereto (the “Existing Credit Agreement”), and terminated all commitments thereunder. The termination of the Existing Credit Agreement became effective at the effective time of the Merger (the “Effective Time”) on August 27, 2018.*

![img3](https://github.com/cth127/cth127.github.io/blob/master/image/NLP101_01_img3.jpg?raw=true)

우리가 원하는 '누가 무엇을 어떻게 했다'는 식의 정보는 추출하지 않고, 단순히 문서에 등장한 named entity나 날짜, 금액 등의 정보를 열거하는 형식이긴 하지만 나름대로 활용할 수 있는 여지는 있어 보인다. 혹은 그 소스코드를 분석하여 이후 IE task에 적용할 여지 또한 있어 보인다.

## 4. Outro

위 글을 통해 우리는 spaCy의 기본적인 구조와 LexNLP의 존재에 대해 알아보았다. 이후의 글에서는 spaCy와 NLTK를 통해 여러 NLP task를 실습해보도록 한다.
