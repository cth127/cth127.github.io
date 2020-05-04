---
title: "NLP - 07 K-means Clustering on Embedding Vector"
date: 2020-05-05
categories: NLP
tags: Embedding
---

# 1. Intro

오늘날 잘 모르는 내 입장에서 보면 NLP든 Computer Vision이든 성능이 컴퓨팅 파워에 의존하는 경향이 있다. 이는 어쩌면 딥러닝이 컴퓨팅 파워의 비약적 상승에 기대어 주목받기 시작했다는 점을 생각해보면 그렇게 놀라울 일도 아니다. 한편 이러한 경향 아래 데이터의 차원이 커짐으로 인해 나타나는 '차원의 저주' 또한 무시할 수 없는 문제가 되었다. 통계학은 오래 전부터 이 문제를 해결하기 위해 PCA, Ridge, Lasso 등 많은 기법을 개발해왔다.

한편 필자는 text categorizatoin 작업을 수행하면서 단어 간 상관관계를 살피기 위해 불필요하게 많아보이는 6만 개의 bag of words(BOW)를 줄일 수 있는 방법을 탐구했고, Embedding 기법이 비슷한 의미를 담는 단어들을 비슷한 좌표에 위치시킨다는 점에 착안, 좌표 간 거리를 중심으로 Clustering을 하는 비지도학습 알고리즘인 K-means clustering이 BOW의 차원을 줄이는 데 도움을 줄 것으로 기대하며 실험을 시작했다.

# 2. Setting

텍스트는 Newswire의 기사 title이며, tf.keras의 lstm layer(256 node, 0.2 dropout, 8 epoch, 500 batch size)을 사용했다. Embedding엔 glove에서 제공하는 300 dimension의 pretrained model을 사용했다. K-means clustering엔 sklearn에서 제공하는 default 값을 사용했으며, k값은 2, 4, 8, 16, 32의 순서로 조정해나갔다. 평가 metric엔 f1-score와 accuracy를 사용했다. 

# 3. Results

결과는 다음과 같다.
