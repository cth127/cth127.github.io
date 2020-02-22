---
title: "NLP101 - 01 spaCy & LexNLP"
date: 2020-02-22
categories: NLP101
---

## 1. Intro

앞서 언급했듯 NLTK의 경우 각 함수가 string을 입력받아 그 결과물로 string을 반환하여 직관적으로 그 구조를 이해하기 어렵지 않으나, spaCy의 경우 자체 object를 반환하기에 그 구조를 간단히 살펴볼 필요가 있다. 따라서 본 글에서는 spaCy를 활용하기 이전에 그 구조를 간단히 살펴보고자 한다. 또한 앞서 소개되지는 않았고 인지도도 그렇게 크지는 않지만, Edgar을 통해 훈련됐다고 주장하는 NLP 라이브러리인 LexNLP에 대해 간략히 살펴보도록 한다.

## 2. spaCy

함수의 입력으로 string을 받는 NLTK와 달리 spaCy는 자체적인 Container을 그 입력으로 받는다. Container에는 `Doc`, `Token`, `Span`, `Lexeme` 네 가지가  있다. 

![img1](https://spacy.io/architecture-bcdfffe5c0b9f221a2f6607f96ca0e4a.svg)

이 중 중심이 되는 것은 string으로 이뤄진 문서를 객체화하는 `Doc`이다. [설명 문서](https://spacy.io/api)에 따르면 `Doc`은 문서를 나름의 pipeline을 통해 재구성하여 저장하는 공간이고, `Token`과 `Span`은 그 문서를 설명하는 두 가지 방식이다. `Token`은 문장이나 단어 등 문서를 이루는 의미 단위로 문서를 설명하는 방식이며, `Span`은 우리가 다른 자료형에서 해왔던 것과 비슷한, 숫자를 이용한 인덱싱방식이다. 이 외 `Vocab`과 `Lexeme`은 단어를 인코딩하는 방식인데, 본 지면의 목적과 다르므로 이후 필요하면 서술하기로 한다. 우리가 다루고자 하는 task에서 기억해야 할 건, 우리가 주로 사용할 함수는 주로 `Doc` 객체 수준에서 다뤄진다는 점이다. 그렇다면 `Doc` 객체는 어떻게 만들어지는가?

![img2]https://spacy.io/pipeline-7a14d4edd18f3edfee8f34393bff2992.svg



(작성중)
