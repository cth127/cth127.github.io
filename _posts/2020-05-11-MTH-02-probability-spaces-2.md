---
title: "MTH - 02 Probability Spaces (2)"
date: 2020-05-05
categories: MTH
tags: Probability
use_math: true
---

# 1. $\sigma$-Algebra

우선 $\sigma$-algebra의 정의를 다시 적는다.

1. $\sigma$-algebra : sample space $\Omega$의 부분집합 A의 모임(collection) $\mathcal{F}$가 다음의 세 조건, 
	- $\phi \in \mathcal{F}$
	- $A \in \mathcal{F} \Rightarrow  A^c \in \mathcal{F}$
	- $A_n \in \mathcal{F},\  n = 1, 2... \Rightarrow \bigcup_{n=1}^{\infty}A_n \in \mathcal{F}$  
을 만족시킬 떄 $\mathcal{F}$을 '$\sigma$-algebra'라 한다.

Algebra란 무엇인가? 웹스터 사전은 algebra를 다음과 같이 정의하고 있다.

- *"any of various systems or branches of mathematics or logic concerned with the properties and relationships of abstract entities (such as complex numbers, matrices, sets, vectors, groups, rings, or fields) manipulated in symbolic form under operations often analogous to those of arithmetic"*

...그만 알아보자.

잘은 모르겠지만 어떤 관계나 성질, 논리, 연산(국문 위키에 따르면 공리) 등을 따르는 추상적인 개체들을 묶어 algebra라고 하는 것 같다. 예컨대 우리는 정수가 덧셈과 곱셈에 대해 닫혀있고, 결합, 교환 법칙 등이 성립함을 알고 있다. 이를 정수의 대수적(algebraic) 성질이라 하는데, 우리가 논하고자 하는 용어와 우연히 겹친 것은 아닐 것이다. 그런 시각에서 보면 위의 여러 algebra 개념도, 낯설긴 하지만, 어떤 논리를 따르는 개체들을 설명하고 있음을 알 수 있다.

한편 Shreve는 $\sigma$-algebra에 대한 조금 더 직관적이고 확률론과 연결된 이해를 돕기 위해 information 개념을 사용한다.

- *"The hedge must specify what position we will take in the underlying security at each future time contingent on how the uncertainty between the present time and that future time is resolved. In order to make these contingency plans, we need a way to mathematically model the information on which our future decisions can be based."* (Shreve, 49p)

예컨대 우리는 동전을 던지기 전엔 그 앞면이 나올지, 뒷면이 나올지 알 수 없다. 하지만 적어도 우린 앞면이나 뒷면 중 하나가 나온다는 것은 알고 있다. 그렇기 때문에 우린 동전 던지기를 수학적 모델로 구성할 수 있다. 뿐만 아니라 주사위를 던졌을 때 가능한 결과들의 집합 {1, 2, 3, 4, 5, 6}이 sample space $\Omega$라면, 이를 통해 우린 우리가 원하는 정보값, 예컨대 {odd, even}, {prime number, o.w.} 등으로 재구성할 수 있으며, 이론상 0부터 무한대까지 가능한 주식의 가격 또한 {상승, 하락}이라는 정보값, 혹은 $\sigma$-algebra로 재구성할 수 있다(물론 그 재구성에 $\phi$와 $\Omega$도 포함되어야 $\sigma$-algebra의 정의를 충족시키며, 이 맥락에서 단순히 {$\phi$, $\Omega$}로만 이뤄진 $\sigma$-algebra는 그 정의를 충족시키긴 하나 별달리 유의미한 정보값을 갖지 못한다). 

그렇다면 $\sigma$-algebra는 왜 저렇게 이상하게 정의가 됐을까? 그 성질을 하나하나 뜯어보면 이해 못할 것도 없다. 예컨대 첫 번째, $\phi \in \mathcal{F}$ 조건은 우리가 관심 없는(예컨대 주사위에서 7이 나온다든지) 부분의 확률에 대해 $\mathbf{P}(\phi) = 0$의 값을 할당하기 위해서이고, 두 번째, $A \in \mathcal{F} \Rightarrow A^c \in \mathcal{F}$ 조건은 우리가 관심 있는 사건과 관심 없는 사건의 확률의 합을 1로 만들기 위해서라고도 할 수 있다. 즉 우리가 주사위에서 홀수가 나오는 사건에만 관심이 있다고 해도, 이를 구성하기 위해선 관심 없는 짝수가 나오는 사건의 확률값(1/2)도 고려를 해야 홀수가 나오는 사건의 확률값(1/2)을 수학적으로 구성할 수 있기 때문이다.

다만 조금 난해해 보이는 것은 세 번째, $A_n \in \mathcal{F},\ n = 1, 2... \Rightarrow \bigcup_{n=1}^{\infty}A_n \in \mathcal{F}$ 조건인데, 이것은 뒤에서 다루게 될 measure와의 관계를 이루기 위한 '좋은 성질'(이 단어를 꽤 많이 쓰게 될 것인데, 왜냐하면 대부분의 정의는 좋은 성질을 가지게 하기 위해 이뤄지기 때문이다)을 갖게 하기 위함이라고만 설명하고 넘어간다. 뒤로 돌아가서 measure의 정의를 보면 위 조건과 꽤 비슷한 요소를 발견할 수 있을 것이다. 

이제 한 가지, 그럼 지난 글에서 다룬 semi-algebra, algebra와는 무슨 관계에 있는 것인지를 규명하는 일만 남았다. 우리의 목적은 어쨌든 연역적으로 확률을 이해하는 것이기 때문이다. 일단 semi-algebra와 algebra, 그리고 $\sigma$-algebra의 정의를 살펴보면 몇 가지 차이점을 발견할 수 있다. 정의는 항상 중요하므로 다시 적는 것도 나쁘지 않을 것 같다.

1. semi-algebra : 집합들의 모임 $\mathcal{S}$이 다음 세 조건,
	- $\phi \in \mathcal{S}$
	- $S, T \in \mathcal{S} \Rightarrow S \cap T \in \mathcal{S}$
	- $S \in \mathcal{S} \Rightarrow S^c\text{ is a finite disjoint union of sets of } \mathcal{S}$  
을 만족시킬 때, $\mathcal{S}$를 'semi-algebra'라 한다.

1. algebra : 집합들의 모임 $\mathcal{A}$이 다음의 세 조건,
	- $\phi \in \mathcal{A}$
	- $A, B \in \mathcal{A} \Rightarrow A \cup B \in \mathcal{A}$
	- $A \in \mathcal{A} \Rightarrow A^c \in \mathcal{A}$  
을 만족시킬 때, $\mathcal{A}$를 'algebra'라 한다.

1. $\sigma$-algebra : sample space $\Omega$의 부분집합 A의 모임(collection) $\mathcal{F}$가 다음의 세 조건, 
	- $\phi \in \mathcal{F}$
	- $A \in \mathcal{F} \Rightarrow  A^c \in \mathcal{F}$
	- $A_n \in \mathcal{F},\  n = 1, 2... \Rightarrow \bigcup_{n=1}^{\infty}A_n \in \mathcal{F}$  
을 만족시킬 떄 $\mathcal{F}$을 '$\sigma$-algebra'라 한다.

보면 공집합을 포함한다는 성질을 공유하고 있고, 세 개념 모두 finite intersection에 대해 닫혀 있으며(algebra와 $\sigma$-algebra의 경우 finite union을 통해 정의돼있지만, 세 번째 성질과 드모르간 법칙을 이용하면 finite union과 finite intersection이 동치임을 쉽게 알 수 있다), 여집합에 대해 어떤 조건을 걸고 있다. 다만 두 번째 조건에 대해 $\sigma$-algebra는 countable union으로 그 조건이 더 좁혀져있고, 여집합 또한 포함하는 나머지 둘과 달리 semi-algebra는 직관적으로 이해하기 힘든 성질을 여집합에 부여하고 있다.

한 가지 힌트를 던지자면, 무한의 세계와 유한의 세계 사이엔 넘사벽이 존재해서, 어떤 개념의 성질을 무한의 세계 내에서 설명하는 건 굉장히 어려운 일이 된다. 그 반대로 유한의 세계에서 그 성질을 설명하는 건 상대적으로 쉬워지며, 우리가 만약 유한의 세계와 무한의 세계 사이의 관계를 알고, 둘을 잇는 조건들을 알게 된다면, 그리고 이를 통해 그 설명을 무한의 세계까지 확장시킬 수 있다면 우린 굉장히 강력한 도구를 얻게 되는 것이다. 쉬운 성질의 조합을 통해 어려운 성질을 증명해내는 것이다! 

그러자면 먼저 우린 semi-algebra에서 시작하여 $\sigma$-algebra까지 개념이 확장되는 과정을 먼저 알아야 한다. 다만 이 과정에서 measure 개념의 확장 또한 함께 이뤄지므로 이를 같이 알아보는 것이 좋다.

# 2. Measure

먼저 앞서 했던 것처럼 measure에 관련된 몇 가지 정의를 적는 것에서부터 시작한다.

1. measure on algebra : algebra $\mathcal{A}$에 대해 함수 $\mu_\mathcal{A} : \mathcal{A} \rightarrow [0, \infty)$가 다음 두 조건,
	- $\mu_\mathcal{A}(A) \geq \mu_\mathcal{A}(\phi) = 0,\ \forall A \in \mathcal{A}$
	- $\bigcup_{i=1}^{\infty}(A_i) \in \mathcal{A} \Rightarrow \mu_\mathcal{A}(\bigcup_{i=1}^{\infty}(A_i)) = \sum_{i=1}^{\infty}\mu_\mathcal{A}(A_i)$  
$\text{ for pairwise disjoint }A_i,\ i=1,2...$  
을 만족시킬 때, 함수 $\mu_\mathcal{A}$를 'measure on algebra'라 한다.

1. $\sigma$-finite : measure on algebra $\mathcal{A}$, $\mu_{\mathcal{A}}$에 대해 수열 $A_i \in \mathcal{A}$  
$s.t.\ \mu_{\mathcal{A}}(A_i)<\infty\ \&\ \bigcup_{i=1}^{\infty}A_i=\Omega$이 존재하면 $\mu_\mathcal{A}$가 $\sigma$-finite하다고 한다.

1. measure : $\sigma$-algebra $\mathcal{F}$에서 양의 실수로 가는 함수 $\mu : \mathcal{F} \rightarrow [0, \infty)$가 다음의 두 조건, 
	- $\mu(\text{A}) \geq \mu(\phi) = 0,\ \forall A \in \mathcal{F}\$ (non-negativity)
	- $A_n \in \mathcal{F},\ n=1,2...,\ A_n\text{ are pairwise disjoint}$  $\Rightarrow \mu(\bigcup_{n=1}^{\infty}A_n) = \sum_{n=1}^{\infty} \mu(A_n)\$ (countable additivity)  
을 만족시킬 때, 함수 $\mu$를 'measure'라 한다.

정의를 훑어봤을 때 measure on algebra와 measure의 정의는 상당히 비슷하지만 단 하나의 조건이 measure on algebra에 붙어있음을 알 수 있으며, 한편 그 조건은 algebra와 $\sigma$-algebra를 나누는 하나의 조건과 밀접한 관련이 있음 또한 알 수 있다. 한편 $\sigma$-finite는 하나의 measure라기보단, $\Omega$를 이루는 $A_i$들에 대한 measure가 실수값으로 존재해야 한다는  measure에 대한 조건에 가깝다는 점을 알 수 있다. 이는 역시 뒤의 정리를 구성하는 조건으로 기능하게 될 것이다. 그럼 이제 measure과 algebra 개념들이 어떻게 좁혀지는지를 살펴보는 일만 남았다.

이 과정에서 필요한 몇 가지 정리를 먼저 적는다. 이전글의 서두에서 말했듯 개별 Theorm, Lemma의 증명은 책에 넘기고, 그 의미 관계를 파악하는 데 집중하고자 한다. 

- Lemma 1.1.7 : semi-algebra $\mathcal{S}$에 대해  $\bar{\mathcal{S}}$ = {finite disjoint unions of sets in $\mathcal{S}$}라 할 때, $\bar{\mathcal{S}}$는 algebra다. 이때 $\bar{\mathcal{S}}$를 "algebra generated by $\mathcal{S}$"라 정의한다. (pf in 4p)

- Definition : semi-algebra $\mathcal{S}$에서 정의된 함수 $\mu$와  $\bar{\mathcal{S}}$ : algebra generated by $\mathcal{S}$, 그리고 집합 $A \in \bar{\mathcal{S}}$에 대해 $A = \bigcup_{n=1}^{n}S_i \text{, where } S_i \in \mathcal{S} \text{ and } S_i\text{'s are pairwise disjoint}$이면, $\bar{\mathcal{S}}$에서 정의된 함수 $\bar{\mu(A)} = \sum_{i=1}^{k} \mu(S_i)$를 함수 $\mu$의 'extended function', 혹은 'extension'이라 정의한다.

- Theorm 1.1.9.a :  semi-algebra $\mathcal{S}$에서 정의된 함수 $\mu$가 다음 세 조건,
	- $\mu(A) \geq \mu(\phi) = 0 \text{ for } \forall A \in \mathcal{S}$
	- If a set S = $\sum_{i=1}^{k} S_i \Rightarrow \mu(S) = \sum_{i=1}^{k} \mu(S_i)$
	- If a set S = $\sum_{i=1}^{\infty} S_i \Rightarrow \mu(S) \geq \sum_{i=1}^{k} \mu(S_i)$
	을 만족시키면, $\bar{\mathcal{S}}$ : algebra generated by $\mathcal{S}$에 대해 유일한 measure on algebra, $\bar{\mu}$가 존재한다. 이때 $\bar{\mu}$는 $\mu$의 extension이다. (pf in 5p)

- Theorm 1.1.9.b : Theorm 1.1.9.a의 조건을 만족시키면서 동시에 $\bar{\mu}$ : $\sigma$-finite 하면, $\sigma(\mathcal{S})$ : the smallest $\sigma$-algebra containing $\mathcal{S}$에 대한 유일한 measure, $\tilde{\mu}$가 존재한다. 이때 $\tilde{\mu}$는 $\bar{\mu}$의 extension이다. (pf in 5p)


- Lemma 1.1.10 :  semi-algebra $\mathcal{S}$에서 정의된 함수 $\mu$가 다음 두 조건,
	- $\mu(A) \geq \mu(\phi) = 0 \text{ for } \forall A \in \mathcal{S}$
	- If a set S = $\sum_{i=1}^{k} S_i \Rightarrow \mu(S) = \sum_{i=1}^{k} \mu(S_i)$
	을 만족시키면, $\bar{\mathcal{S}}$ : algebra generated by $\mathcal{S}$에서 정의된 함수, $\bar{\mu}$ : extension of $\mu$는 집합 A, $B_i \in \bar{\mathcal{S}}에 대해 다음의 두 성질을 가진다.
	- If $A = \bigcup_{i=1}^{n}B_i \Rightarrow \bar{\mu}(A) = \sum_{i=1}^{n}(B_i)$
	- If $A \subset \bigcup_{i=1}^{n}B_i \Rightarrow \bar{\mu}(A) \geq \sum_{i=1}^{n}(B_i)$

(작성중)
