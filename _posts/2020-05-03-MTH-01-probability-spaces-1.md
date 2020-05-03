---
title: "MTH - 01 Probability Spaces (1)"
date: 2020-05-03
categories: MTH
tags: PROB
use_math: true
---

# 1. Intro

본 글의 목적은 확률론을 수학적으로 이해하는 것이다. 필자가 통계학과 학부에서 들었던 확률론은 직관적으로 이해 가능한 범주의 내용이었다. 하지만 수학과 대학원에서 듣는 확률론 수업(교재는 Durrett의 책)은 직관의 범주를 뛰어넘는 것이었고, 사실 아직까지 필자의 이해가 적절한 건지 잘 모르겠다. 그래서 이 글은 필자 나름의 이해를 담아 정리한 글일뿐, 정확도는 담보되지 않는다. 

본 글은 어디까지나 본 블로그의 목적인, 배운 내용의 정리를 위한 글이고, 각 개념 및 theorm 사이의 큰 그림을 파악하는 데 그 목적을 두며, 개별 theorm이나 lemma 대한 세세한 증명은 링크, 혹은 교재의 페이지로 대체한다. 같은 맥락에서 이야기를 풀어나가는 데 크게 유용해보이지 않는 요소는 생략될 수 있으니, 좀 더 정확한 지식을 얻고 싶다면 [Durrett 선생이 온라인 배포한 교재](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf)를 참고하길 바란다.

# 2. Concept

우선 본 글에서 담고자 하는 개념을 나열하는 것으로 시작한다. 번역의 문제를 피하기 위해 주요 용어는 교재에서 사용한 영어를 차용한다.

1. sample space : 실험에서 가능한 결과들의 집합 $\Omega$를 'sample space'라 한다. 

1. event : sample space $\Omega$의 부분집합 A를 'event'라 한다.

1. $\sigma$-algebra : sample space $\Omega$의 부분집합 A의 모임(collection) $\mathcal{F}$가 다음의 세 조건, 
	- $\phi \in \mathcal{F}$
	- $A \in \mathcal{F} \Rightarrow  A^c \in \mathcal{F}$
	- $A_n \in \mathcal{F},\  n = 1, 2... \Rightarrow \bigcup_{n=1}^{\infty}A_n \in \mathcal{F}$  
을 만족시킬 떄 $\mathcal{F}$을 '$\sigma$-algebra'라 한다.

1. measure : $\sigma$-algebra $\mathcal{F}$에서 양의 실수로 가는 함수 $\mu : \mathcal{F} \rightarrow [0, \infty)$가 다음의 두 조건, 
	- $\mu(\text{A}) \geq \mu(\phi) = 0,\ \forall A \in \mathcal{F}\$ (non-negativity)
	- $A_n \in \mathcal{F},\ n=1,2...,\ A_n\text{ are pairwise disjoint}$  $\Rightarrow \mu(\bigcup_{n=1}^{\infty}A_n) = \sum_{n=1}^{\infty} \mu(A_n)\$ (countable additivity)  
을 만족시킬 때, 함수 $\mu$를 'measure'라 한다.

1. probability :  sample space $\Omega$와 그 $\sigma$-algebra $\mathcal{F}$에 대해, measure $\mathbf{P} : \mathcal{F} \rightarrow [0, 1]$(codomain이 다름에 주의!)가 다음의 한 조건,
	- $\mathbf{P}(\Omega) = 1$  
을 만족시킬 때, 함수 $\mathbf{P}$를 'probability'라 한다.

1. spaces : 위의 기호를 차용했을 때  ($\Omega, \mathcal{F}$)를 'measurable space',  ($\Omega, \mathcal{F}, \mu$)를 'measure space',  ($\Omega, \mathcal{F},  \mathbb{P}$)를 'probability space'라 한다.


이러한 주개념을 전개하기 위해 다음과 같은 개념들 또한 필요하다.

1. semi-algebra : 집합들의 모임 $\mathcal{S}$이 다음 세 조건,
	- $\phi \in \mathcal{S}$
	- $S, T \in \mathcal{S} \Rightarrow S \cap T \in \mathcal{S}$
	- $S \in \mathcal{S} \Rightarrow S^c\text{ is a finite disjoint union of sets of } \mathcal{S}$  
을 만족시킬 때, $\mathcal{S}$를 'semi-algebra'라 한다.

1. algebra : 집합들의 보임 $\mathcal{A}$이 다음의 세 조건,
	- $\phi \in \mathcal{A}$
	- $A, B \in \mathcal{A} \Rightarrow A \cup B \in \mathcal{A}$
	- $A \in \mathcal{A} \Rightarrow A^c \in \mathcal{A}$  
을 만족시킬 때, $\mathcal{A}$를 'algebra'라 한다.

1. measure on algebra : algebra $\mathcal{A}$에 대해 함수 $\mu_\mathcal{A} : \mathcal{A} \rightarrow [0, \infty)$가 다음 두 조건,
	- $\mu_\mathcal{A}(A) \geq \mu_\mathcal{A}(\phi) = 0,\ \forall A \in \mathcal{A}$
	- $\bigcup_{i=1}^{\infty}(A_i) \in \mathcal{A} \Rightarrow \mu_\mathcal{A}(\bigcup_{i=1}^{\infty}(A_i)) = \sum_{i=1}^{\infty}\mu_\mathcal{A}(A_i)$  
$\text{ for pairwise disjoint }A_i,\ i=1,2...$  
을 만족시킬 때, 함수 $\mu_\mathcal{A}$를 'measure on algebra'라 한다.

1. $\sigma$-finite : measure on algebra $\mathcal{A}$, $\mu_{\mathcal{A}}$에 대해 수열 $A_i \in \mathcal{A}$  
$s.t.\ \mu_{\mathcal{A}}(A_i)<\infty\ \&\ \bigcup_{i=1}^{\infty}A_i=\Omega$이 존재하면 $\mu_\mathcal{A}$가 $\sigma$-finite하다고 한다.

1.  the Borel $\sigma$-field : 실수 집합 $\mathbb{R}$의 모든 열린 부분집합을 포함하는 최소한의 $\sigma$-field를 'Borel $\sigma$-field'라 하고, $\mathcal{B}(\mathbb{R})$, 또는 $\mathcal{R}$로 쓴다.

1. Stieltjes measure function : 함수 $F:\mathbb{R}\rightarrow\mathbb{R}$가 다음 두 조건,
	- $F\text{ is nondecreasing}$
	- $F\text{ is right continuous, }$  
	  $i.e.\ x_i\to x^+ \Rightarrow \lim_{i\to\infty}F(x_i)=F(x)$  
을 만족시킬 때, 함수 $F$를 'Stieltjes measure function'이라 한다.

1. 'Lebeque measure' : 임의의 Stieltjes measure function $F$에 대해 measurable space ($\mathbb{R}, \mathcal{R}$)에서 정의된 measure $\mu\ s.t.\ \mu((a,b]) = F(b) - F(a)$가 유일하게 존재한다. 이때 $F(x) = x$이면 measure $\mu((a,b]) = b - a$를 'Lebeque measure'라 한다.


# 3. Motive

도대체 왜 이런 개념들이 필요한가에 대한 의문이 들 수 있다. 학부 수준에서 사용하는 Bertesekas의 확률론 교재나 Hogg의 수리통계학 교재에선 기초적인 집합론을 다룬 이후, sample space와 events를 간략하게 정의한 뒤 바로 확률의 공리적 정의를 다룬다. (그 공리 세 가지 중 두 가지인 nonnegativity와 countable additivity가 사실 measure의 정의에서 나온 것임은 어렵지 않게 확인할 수 있다.) 이 책들은 sample space의 부분집합이 각각 확률이라는 함수 $\mathbf{P}$에 입력돼서 [0, 1] 사이의 실수값을 갖게 되는 과정을 별다른 부가설명 없이 보여주고 넘어가는데, 확률의 개념을 대략적으로 알고 있는 우린 나름 어렵지 않게 그 개념을 받아들일 수 있다. 하지만 우리가 아무것도 모르는 백지 상태에서 이 개념들을 연역적으로 이해해나갈 수 있을까?

예를 들면 sample space의 부분집합은 무엇이고 어떤 성질을 갖길래 함수 $\mathbf{P}$의 입력 값이 될 수 있는지, $\mathbf{P}$라는 함수는 왜 갑자기 공리의 형식으로 등장할 수 있는지, 그러한 공리적 성질은 무엇에 기반한 것인지, 왜 그런 성질이 필요한 것인지, 그래서 $\mathbf{P}$는 무엇을 의미하는 것인지를 동전 던지기나 주사위 던지기 같은 경험적 확률에 빗대지 않고 설명하기는 위의 개념들만을 가지고는 부족한 일일 것이다. 이산 확률이야 그렇다 쳐도 연속 확률의 경우는 어떠한가? $\mathbf{P}$의 입력값, 즉 정의역이 sample space의 부분집합이라면, 연속형인 sample space에서 모든 가능한 부분집합을, 일반성을 잃지 않으면서(w.o.l.g.) 어떻게 설명할 수 있는가? Hogg는 이와 관련하여 1.3절 초입부에 다음과 같은 힌트를 남겼다.

- *"What should be our collection of events? If $\mathcal{C}$ is a finite set, then we could take the set of all subsets as this collection. For infinite sample spaces, though, with assignment of probabilities in mind, this poses mathematical technicalities which are better left to a course in a probability theory."* (Hogg, 10p)

우리가 이 글에서 주목해야 할 것은 확률을 직관에 의존하지 않고 설명할 수 있는 방법이다. 그런 이후에야 우린 나중의 random variable이나 distribution, independence같은 주요한 개념 역시 직관에 의존하지 않고 설명할 수 있을 것이다. 그런 맥락에서 우리가 가장 먼저 부딪히게 되는 비직관적인 개념은 $\sigma$-algebra이다.

따라서 우린 앞으로 (1) semi-algebra, algebra로부터 $\sigma$-algebra를 구체화시켜 나가는 방식으로 이해해나갈 것이다. (2) 또한 그렇게 좁혀지는 개념들 속에서 마찬가지로 좁혀지는 함수를 관찰할 것이고, 그것이 우리가 정의한 measure로 구체화되는 과정을 지켜봄과 동시에, (3) 그 하나로서 확률 $\mathbf{P}$, 그리고 본 글의 제목인 probability space의 정의와 성질, 그리고 의미를 곱씹어볼 것이다. (4) 그리고 그곳에 사용되는 논리가 Stieltjes measure function에서 앞으로 우리가 자주 사용하게 될 Lebeque measure로 좁혀지는 데에도 적용될 수 있음을 확인하면서, (5) 여유가 된다면 measure의 차원이 확장되는 데 필요한 트릭 또한 살펴보고자 한다.
