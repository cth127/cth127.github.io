---
title: "MTH - 01 Probability Spaces"
date: 2020-05-03
categories: MTH
tags: PROB
use_math: true
---

# 1. Intro

본 글의 목적은 확률론을 수학적으로 이해하는 것이다. 필자가 통계학과에서 들었던 확률론은 직관적으로 이해 가능한 범주의 내용이었다. 하지만 수학과 대학원 과정에서 듣는 확률론 수업(교재는 Durrett의 책)은 직관의 범주를 뛰어넘는 것이었고, 사실 내 이해가 괜찮은 건지 잘 모르겠다. 그래서 이 글은 필자의 이해를 담아 정리한 글일뿐, 정확도는 담보되지 않는다. 어디까지나 본 블로그의 목적인, 배운 내용의 정리를 위한 글이다.

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
	- $A_n \in \mathcal{F},\ n=1,2...,\ A_n\ are\ pairwise\ disjoint$ $\Rightarrow \mu(\bigcup_{n=1}^{\infty}A_n) = \sum_{n=1}^{\infty} \mu(A_n)\$ (countable additivity)  
을 만족시킬 때, 함수 $\mu$를 'measure'라 한다.

1. probability :  sample space $\Omega$와 그 $\sigma$-algebra $\mathcal{F}$에 대해, measure $\mathbb{P} : \mathcal{F} \rightarrow [0, 1]$(codomain이 다름에 주의!)가 다음의 한 조건,
	- $\mathbb{P}(\Omega) = 1$  
을 만족시킬 때, 함수 $\mathbb{P}$를 'probability'라 한다.

1. spaces : 위의 기호를 차용했을 때 ($\Omega, \mathcal{F}$)를 'measurable space', ($\Omega, \mathcal{F}, \mu$)를 'measure space',  ($\Omega, \mathcal{F}, \mathbb{P}$)를 'probability space'라 한다.


이러한 주개념을 전개하기 위해 다음과 같은 개념들 또한 필요하다.

1. semi-algebra : 집합들의 모임 $\mathcal{S}$이 다음 세 조건,
	- $\phi \in \mathcal{S}$
	- $S, T \in \mathcal{S} \Rightarrow S \cap T \in \mathcal{S}$
	- $S \in \mathcal{S} \Rightarrow S^c\text{ is a finite disjoint union of sets of } \mathcal{S}  
을 만족시킬 때, $\mathcal{S}$를 'semi-algebra'라 한다.

1. algebra : 집합들의 보임 $\mathcal{A}$이 다음의 세 조건,
	- $\phi \in \mathcal{A}$
	- $A, B \in \mathcal{A} \Rightarrow A \cup B \in \mathcal{A}$
	- $A \in \mathcal{A} \Rightarrow A^c \in \mathcal{A}  
을 만족시킬 때, $\mathcal{A}$를 'algebra'라 한다.

1. measure on algebra : algebra $\mathcal{A}$에 대해 함수 $\mu_\mathcal{A} : \mathcal{A} \rightarrow [0, \infty)$가 다음 두 조건,
	- $\mu_\mathcal{A}(A) \geq \mu_\mathcal{A}(\phi) = 0,\ \forall A \in \mathcal{A}$
	- $\bigcup_{i=1}^{\infty}(A_i) \in \mathcal{A} \Rightarrow \mu_\mathcal{A}(\bigcup_{i=1}^{\infty}(A_i)) = \sum_{i=1}^{\infty}\mu_\mathcal{A}(A_i)$  
$\text{ for pairwise disjoint }A_i,\ i=1,2...$  
을 만족하시킬 때, 함수 $\mu_\mathcal{A}를 'measure on algebra'라 한다.

1. $\sigma$-finite : measure on algebra $\mathcal{A}$, $\mu_{\mathcal{A}}에 대해 수열 $A_i \in \mathcal{A}$  
$s.t.\ \mu_{\mathcal{A}}(A_i) < \infty \& \bigcup_{i=1}^{\infty}A_i=\Omega$이 존재하면 $\mu_\mathcal{A}$가 $\sigma$-finite하다고 한다.

1.  the Borel $\sigma$-field : 실수 집합 $\mathbb{R}$의 모든 열린 부분집합을 포함하는 $\sigma$-field를 'Borel $\sigma$-field'라 하고, $\mathcal{B}(\mathbb{R})$, 또는 $\mathcal{R}$로 쓴다.

1. Stieltjes measure function : 함수 $F:\mathbb{R}\rightarrow\mathbb{R}$가 다음 두 조건,
	- $F\ is\ nondecreasing$
	- $F\ is\ right\ continuous,\ i.e.\ x_i\to x^+ \Rightarrow \lim_{i\to\infty}F(x_i)=F(x)$  
을 만족시킬 때, 함수 F를 'Stieltjes measure function'이라 한다.

1. 'Lebeque measure' : 임의의 Stieltjes measure function $F$에 대해 measurable space ($mathbb{R}, \mathcal{R}$)에서 정의된 measure $\mu\ s.t.\ \mu((a,b]) = F(b) - F(a)$가 유일하게 존재한다. 이때 $F(x) = x$이면 measure $\mu((a,b]) = b - a$를 'Lebeque measure'라 한다.
