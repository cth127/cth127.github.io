---
title: "FEN - 04 Contango & Normal Backwardation "
date: 2020-04-15
categories: FEN
tags: Pricing
---

# 1. Contango and Normal Backwardation

  선물 시장엔 다양한 동기를 가진 참여자가 있지만, 주로 자신이 가진 자산에 대한 리스크를 헷지하고자 하는 hedger과 선물 가격의 가격에 베팅하는 speculator이 있다. Hedger와 speculator는 서로 같은 가격에 거래함에도 불구하고 져야 하는 리스크가 서로 다르다. 애초에 hedger가 선물 시장에 참여하는 목적이 speculator에게 자신의 리스크를 전가하기 위해서이기 때문이다. 이로 인해 speculator는 더 많은 리스크를 부담하게 되고, 따라서 그 리스크만큼의 리스크 프리미엄을 요구하게 된다. 이것이 선물 가격에 나타나는 형태가 contango와 normal backwardation이다.
	
  용례에 따라 다르긴 하지만, Hull에 따르면 contango는 현재의 선물 가격이 미래에 기대되는 현물 가격보다 비싼 (F0 > E(ST)) 경우를 말하고, normal backwardation은 반대로, 선물 가격이 미래에 기대되는 현물 가격보다 싼 (F0 < E(ST)) 경우를 말한다. 위의 설명은 Keynes와 Hicks의 경제학적 설명으로, hedger가 speculator에 비해 상대적으로 롱 포지션에 많을 경우 더 많은 리스크 프리미엄을 져야 하는 쪽은 숏 포지션이므로, 선물 가격이 더 높은 contango 현상이 나타나고, 반대로 hedger가 숏 포지션에 더 많을 경우 normal backwardation이 나타난다는 것이다.
	
  한편 오늘날 CAPM 모형과 결합하여 설명하는 이론이 있는데, 이는 해당 상품이 시장의 구조적 리스크와 어떤 상관관계를 가졌는지, 그리고 시장에 구조적 위험이 존재하는지에 따라 contango와 normal backwardation이 일어날 수 있다고 본다. CAPM에 따르면 충분히 분산된 포트폴리오는 개별 자산의 리스크가 아닌, 시장 전체의 구조적에만 영향을 받는다. 예상되는 포트폴리오의 수익률을 k, 자금을 조달할 수 있는 무위험 이자율을 r이라고 한다면, t=0 시점에 현물가 S0는 E(ST)\*e^-k로 할인한 것이고, 이는 선물가를 할인한 F0\*e^-r과 균형을 이뤄야 한다. 이 식을 풀면 F0 = E(ST)\*e^-(r-k)T가 되고, r과 k의 대소관계에 따라 F0와 E(ST)의 대소관계가 정해진다.
	
  풀어서 말하자면, 만약 우리가 거래하려 하는 포트폴리오가 시장의 구조적 위험과 양의 상관관계를 가지고 있다고 가정했을 때, 시장의 수익률이 무위험 이자율보다 높다면 선물가보다 기대 현물가가 높은 normal backwardation, 반대로 시장 수익률이 무위험 이자율보다 낮다면 선물가보다 기대 현물가가 낮은 contango 현상이 일어나는 것이다.
	
  하지만 시간이 만기에 가까워질수록 현물가와 선물가는 수렴하는 경향이 있으므로, 상대적으로 고평가된 상품에 숏 포지션을 잡고, 상대적으로 저평가된 상품에 롱 포지션을 잡는 무위험 차익 거래 기회가 존재할 수 있다. 즉, 선물 가격이 고평가 된 contango 상황에선 선물에 숏, 현물에 롱 포지션을 잡음으로써 수익을 얻을 수 있고, 반대의 normal backwardation 상황에선 그 반대의 포지션을 잡음으로써 수익을 얻을 수 있는 것이다.

# 2. Current Backwardation in KOSPI 200

  위에 비춰보면 최근 한국 시장에서 나타나고 있는 backwardation 현상 역시 두 가지 관점에서 설명될 수 있다. 먼저 Keynes의 관점에서 보면 현재 한국 선물 시장엔 hedger가 주로 숏 포지션을, speculator가 주로 롱 포지션을 점하고 있는 것이다. 한동안 코로나로 인해 내리막을 걸은 한국 증시가 반등할 것이라는 speculator가 롱 포지션에 참여하기 위해선 hedger가 부담하는 리스크를 부담할 수 있을 만큼의 리스크 프리미엄이 존재해야 하고, 선물 시장의 낮은 가격은 이를 반영하고 있는 것이다.
	
  한편 두 번째로는 그만큼 현재 시장에 참여했을 때 기대되는 시장의 수익률이 높다고도 할 수 있다. 낙폭이 큰 만큼 상승할 여지도 큰 것이다. 더군다나 세계적으로 행해지는 양적 완화로 인해 이자율이 낮아지는 상황에서 수익률 k가 무위험 이자율 r을 상회하게 되고, 이로 인해 선물 가격이 현물 가격을 밑돌게 되는 것이다.
	
  이러한 이론적 설명 외에도 정부의 공매도 금지로 인한 시장 가격 왜곡 또한 원인으로 지적되고 있다. 개인적인 생각으론 흔히 ‘동학 개미 운동’으로 표현되는 개인들의 매수 또한 그 역할을 하고 있는 것으로 보인다. 기관 투자자가 아니면 선물 시장으로의 접근 자체가 어렵기에, 개인의 매수가 강하게 나타나는 현물 시장 가격이 선물 시장 가격을 웃돌고 있다고도 설명할 수 있다.
