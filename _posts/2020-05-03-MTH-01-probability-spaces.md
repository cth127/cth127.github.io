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
	- $\mu(\text{A}) \geq \mu(\phi) = 0,\ \forall A \in \mathcal{F}$ (non-negativity)
	- $A_n \in \mathcal{F},\ n=1,2...,\ A_n\ are\ pairwise\ disjoint$ $\Rightarrow \mu(\bigcup_{n=1}^{\infty}A_n) = \sum_{n=1}^{\infty} \mu(A_n)$ (countable additivity)
을 만족시킬 때, 함수 $\mu$를 'measure'라 한다.
1. probability :  sample space $\Omega$와 그 $\sigma$-algebra $\mathcal{F}$에 대해, measure $\mathbb{P} : \mathcal{F} \rightarrow [0, 1]$(codomain이 다름에 주의!)가 다음의 한 조건,
	- $\mathbb{P}(\Omega) = 1$
을 만족시킬 때, 함수 $\mathbb{P}$를 'probability'라 한다.
1. spaces : 위의 기호를 차용했을 때 ($\omega, \mathcal{F}$)를 'measurable space', ($\omega, \mathcal{F}, \mu$)를 'measure space',  ($\omega, \mathcal{F}, \mathbb{P}$)를 'probability space'라 한다.
