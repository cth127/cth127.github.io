---
title: "NLP - 01 Comparison of NLP Libraries"
date: 2020-02-16
categories: NLP
---

## 1. Intro

<p> 본 글은 Edgar에서 Information Extraction(IE)를 수행하기 위해 필요한 NLP 라이브러리를 찾고, 각 라이브러리가 각각의 task를 
어떤 식으로 수행하는지를 정리하기 위한 글이다. 따라서 본 글은 라이브러리를 설치하는 법이나, 각 task에 대한 구체적인 설명, 
IE의 수행에 필요할 것으로 보이지 않는 task는 다루지 않는다. 각 라이브러리가 샘플 Edgar 텍스트에 대해 각 과제를 어떻게 수행하는지를
관찰하는 것을 목표로 한다. </p>

본 글의 목적에 따라 탐구가 필요한 라이브러리에 대해 다음과 같은 조건을 설정했다. 

  - 파이썬 라이브러리일 것.
  - 어느 정도 그 성능이 검증된, 인지도 있는 라이브러리일 것.
  - Tokenization, NER, POS tagging, Parsing 등 IE에 필요한 task를 모두 수행할 수 있을 것.
  - 상업적 이용이 가능한 오픈소스 라이브러리일 것. 
  - end-to-end 라이브러리일 것.

## 2. Simple Research

### 2-1. [Comparing the Functionality of Open-source Natural Language Processing Libraries](https://blog.dominodatalab.com/comparing-the-functionality-of-open-source-natural-language-processing-libraries/)

<p> 이 글은 Spark NLP, spaCy, NLTK, OpenNLP, Stanford CoreNLP 등 다섯 가지 유력한 end-to-end NLP 라이브러리를 각 기능 및 환경별로 나눠 비교하고 있다. 이 글에 따르면 OpenNLP와 CoreNLP는 Java 기반으로 개발이 이뤄져 위에 언급한 조건에 부합하지 않는다. 또한 CoreNLP는 상업적 이용이 금지되어 있다. 그렇게 남는 것은 SparkNLP, spaCy, NLTK인데, 글의 구성에서도 그렇고 SparkNLP에 대해서 굉장히 호의적인 모습을 보이고 있는 것으로 보아 약간의 광고성(...)이 있다고 판단했다. 이에 본 글은 spaCy와 NLTK 간 비교를 중심으로 리서치를 진행하였다. (아래 표에 따르면 SparkNLP는 spaCy와 NLTK가 제공하지 않는 Spell checker와 Sentiment Detect 기능을 제공하는데, 이는 IE를 수행하기에 필수적이지 않을 것이라는 판단이 있었가에 SparkNLP를 고려대상에서 제외하기 더 쉬웠다.) </p>

![table1](https://blog.dominodatalab.com/wp-content/uploads/2019/04/Pacific-AI-Table-1-cx-Sep-2019.png)

위 표에 따르면 spaCy와 NLTK는 모두 NER, POS tagging, Parsing 등 여러 task를 end-to-end 형식으로 지원하며, 앞서 언급한 다른 모든 조건에도 부합한다. 한편 spaCy의 경우 NLTK에서 지원하지 않는 [Text Matcher](https://spacy.io/usage/rule-based-matching) 기능을 제공하는데, 이를 통해 Rule-based IE를 수행할 수 있다. 많은 NLP task에서 딥러닝 기반의 방식이 기존 Rule-based 방식보다 더 좋은 성능을 내고 있다고 [보고](https://arxiv.org/pdf/1807.02383.pdf)되고는 있지만, Edgar에서와 같이 텍스트가 고도로 정형화된 경우, 그리고 데이터가 딥러닝을 활용할 수 있을만큼 풍부하지 않은 경우엔 Rule-based 방식이 더 좋은 성능을 낼 수 있다.

### 2-2. [NLTK vs spaCy Natural Language Processing in Python](https://blog.thedataincubator.com/2016/04/nltk-vs-spacy-natural-language-processing-in-python/)

이 글에 따르면 spaCy와 NLTK는 다음과 같은 차이를 가진다.

|     | NLTK | spaCy |
|---|:---:|---:|
| 적용모델 | 여러가지를 지원 | 한가지를 지원 |
| 결과물 | string | object |
| 속도 | 느림 | 빠름 |

<p> 정리하자면 spaCy는 Sentence Tokenization을 제외한 task에 대해 속도, 성능 면에서 NLTK에 대해 비교우위를 보인다. 또한 NLTK의 경우 각 task에 대해 여러가지 방법론을 제공하는 한편 spaCy는 개발자가 생각하는 가장 좋은 하나의 방법만을 제시함으로써 언어학에 대한 지식이 상대적으로 부족해도 어렵지 않게 활용할 수 있게 설계되었다. (하지만 이는 반대로 말하자면 텍스트의 성질을 분석하여 가장 효과적인 방법론을 도출해낼 수 있는 기회를 제한한다고도 할 수 있다. 각각의 텍스트 성질에 따라 A 방법론이 더 잘 통할 수도 있는 거고, B 방법론이 더 잘 될 수도 있기 때문이다.) 한편 NLTK는 spaCy에 비해 다양한 언어에 적용될 수 있다는 장점이 있지만, 이번에 다룰 IE task는 영어만을 대상으로 하기에 굳이 적지 않았다. </p>
  
<p> 한편 짧은 블로그 글 몇 편만으로 비교를 마치기엔 부족한 감이 있어서 NLP 라이브러리를 비교한 몇 가지 논문을 살펴보았다. NLTK와 spaCy를 동시에 다룬 논문을 두 편 정도 찾을 수 있었다. </p>

## 3. Deeper Research

### 3-1. [Choosing an NLP Library for Analyzing Software Documentation](https://ieeexplore.ieee.org/abstract/document/7962368)

<p> 이 논문은 Stanford CoreNLP, SyntaxNet, NLTK, spaCy, 네 가지 라이브러리로 Stack Overflow, Github의 Readme.md파일, Java API 문서 세 가지에 대해 tokenization과 POS tagging를 적용하여 그 성능 및 결과를 비교분석한 것이다. 논문은 각 라이브러리가 내놓은 결과물이 얼마나 일치하는지를 비교하고, 사람이 직접 위 task를 수행한 결과물과 비교하여 그 객관적인 성능을 검증한다. 논문에 따르면 tokenization의 경우 대체로 모두 90% 이상의 일치율을 보였지만, POS tagging의 경우엔 최저 68%, 최고 87%의 낮은 일치율을 보였다. 이는 위의 문제에 어느 정도 객관적인 정답이 정해져있다는 것을 생각하면 상당히 의외인 결과라 할 수 있다. </p>

![table 4](https://github.com/cth127/cth127.github.io/blob/master/image/NLP101_00_table4.jpg?raw=true)

<p> 특히 사람이 직접 라벨링을 한 데이터와 비교를 해보면 그 차이가 더욱 잘 드러난다. tokenization의 경우 사용된 라이브러리가 모두 어느 수준 이상의 성능을 내긴 하지만 NLTK가 정확도 면에서 압도적으로 우위를 차지하고 있으며, 특히 Github 문서에 대해 NLTK와 spaCy의 성능차이가 크다. 하지만 POS tagging의 경우 문서나 POS tagging의 종류(g는 general, s는 specific)에 따라 다르긴 하지만, 전반적으로 spaCy가 NLTK에 대해 우위를 점하고 있다.(각 라이브러리는 fine-tuning이 이뤄지지 않은, default 상태에서 사용된 것이며, 저자에 따르면 사람이 직접 행한 작업에 편향이 있을 수도 있다.) 이러한 결과는 각 라이브러리가 자신을 정당화하기 위해 공통적으로 사용한 WSJ data나 Wiki data 등에서 얻은 결과와는 다소 차이가 있다. </p>

![figure 2](https://github.com/cth127/cth127.github.io/blob/master/image/NLP101_00_figure2.jpg?raw=true)

<p> 논문에선 지적되지 않았지만 위의 그림에 따르면 NLTK의 성능은 문서 종류의 차이에 크게 영향을 받지 않아 분산이 적은 모습을 보여주고 있다. 이는 문서 간 성능 차이가 상대적으로 크게 나타나는 spaCy와 대조되는 지점이며, NLTK가, 성능 면에서 부족한 부분도 있긴 하지만, 전체적으로 robust한 모습을 보여주고 있다고도 할 수 있다. 논문의 저자들은 처음엔 Stack Overflow가 개발자들이 서로 편하게 질문을 주고받는 곳이라는 점에서 문법적 오류나 구어표현 등으로 인해 오류가 많을 것이라 예상했는데, 오히려 공식적인 API 문서보다 더 좋은 정확도를 얻고 있다. 저자들에 따르면 이는 API 문서에 컴퓨터 코드 등 일상에서 잘 쓰지 않는 정보가 많이 포함되어 있기 때문일 것으로 보인다. </p>

<p> 논문의 함의를 요약하자면 서로의 성능을 비교하기 위한 보편적인 ground truth도 중요하지만, 그것과는 별개로 task and document specific한 성능의 테스트 또한 중요하다고 할 수 있다. 또한 이 논문에서의 테스트는 위 2-2 글의, spaCy의 성능이 NLTK보다 우위에 있다는 내용과는 차이가 있다. </p>

### 3-2. [A Replicable Comparison Study of NER Software](https://ieeexplore.ieee.org/document/8931850/)

<p> 이 논문은 위에선 다루지 않은 NER을 중심으로 라이브러리를 비교하고 있다. 비교 대상 라이브러리는 Stanford CoreNLP, Gate, OpenNLP, NLTK, spaCy 등이며, CoNLL 2003, GMB data를 대상으로, 그리고 F1 score를 중심 척도로 이뤄졌다. 위 논문에 따르면 NER은 결국 tokenization과 POS tagging을 기반으로 이뤄지는 것이긴 하지만, 어쨌든 지금은 최대한 end-to-end를 지향하고 있기에 NER만을 수행한 논문 또한 본 글에 포함하였다. </p>

![table 3](https://github.com/cth127/cth127.github.io/blob/master/image/NLP101_00_table3.jpg?raw=true)

<p> 본 논문에 따르면 라이브러리 간 차이는 GMB data보다 CoNLL 2003 data에서 더 컸으며, 사람과 지명을 나타내는 PER, LOC 범주보다 집단을 나타내는 ORG 범주에서 더 컸다. (그렇다고 PER과 LOC 범주에서의 차이가 작다는 것은 아니다.) 이는 반갑지 않은 결과인데, 본 프로젝트에서 중심적으로 NER이 이뤄져야 하는 명사는 주로 법인 명 등 ORG 범주에 속하기 때문이다. spaCy와 NLTK에서 모두 ORG에 대한 F1 score는 모두 24~36 정도로, 상업적 활용이 불가능할 정도로 저조하다. fine-tuning에 따라 달라질 수 있긴 하겠지만, 일반적으로 fine-tuning에 의한 성능 차이는 2~3배까지 나지 않는다. 가장 점수가 좋은 Stanford CoreNLP도 GMB data의 ORG 범주에 대해선 57의 저조한 점수를 기록했다. 안정적인 성능을 내기 위해선 end-to-end 방식이 아닌 대안이 필요하다는 것이다. </p>

<p> 한편 흥미로운 점은 CoNLL 2003에선 spaCy가, GMB에선 NLTK가 전반적인 성능의 우위를 점하고 있으며, ORG 범주에 대해선 spaCy가 일관되게 더 좋은 성능을 보인다는 것이었다. 본 논문에서 아쉬웠던 것은 왜 그러한 결과가 나왔으며, 그러한 차이를 유발한 data 상의 issue는 없었는지를 더 탐구하지 않았다는 점이다. </p>

## 4. Outline

위의 내용을 종합해보면 결국 **그때그때 다르다**는 결론을 얻을 수 있다. 이에 이후의 글에서는 Edgar에서 제공하는 한두개의 sample text에 spaCy와 NLTK를 통해 다음 task를 적용해보는 것을 목표로 한다.

  - Sentence tokenization
  - Word tokenization
  - POS tagging
  - Parsing
  - NER

그리고 이후엔 IE에 유용하게 이용할 수 있는 정규표현식를 다뤄보겠다. 이 과정을 시작하기에 앞서 다음 글에서는 spaCy 라이브러리의 기본적인 구조를 살펴보겠다. NLTK의 경우 string을 결과물로 반환하여 직관적으로 그 구조를 이해하기 어렵지 않으나, spaCy의 경우 자체 object를 반환하기에 그 구조를 간단히 살펴볼 필요가 있다.
