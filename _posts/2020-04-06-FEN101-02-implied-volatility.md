---
title: "FEN101 - 02 Implied Volatility of KOSPI200 Call Option"
date: 2020-04-06
categories: FEN101, Pricing
---

# 1. Intro

코로나로 인해 급변하는 주식 시장에서 2020년 5월이 만기인(5월 14일) KOSPI200 call option 가격을 통해 implied volatility를 구하고자 한다. 몬테카를로 시뮬레이션(MCS)을 통해 각 volatility에 따른 KOSPI200의 경로를 10만회 생성하고, 그 결과값을 통해 옵션의 이론가를 구한 뒤, 실제 가격과 MSE를 구해 이를 최소화하는 volatility를 찾으려 한다. 다음은 이 과정에서 필요한 몇 가지 전제이다.

- 주가는 geometric Brownian motion을 따르며, Ito's lemma를 적용한다. 즉, 

$$$S \left( t+dt \right)=S \left( t \right) \exp \left[ \left( r- {\sigma ^2 \over 2} \right) dt + \sigma \sqrt{dt}Z \right], where Z \sim N(0, 1)$$$

의 과정을 따른다. 관련해서는 확률미적분학과 확률론 관련 포스팅에서 다룬다.
- 이에 필요한 변수로 $$r=0.011$$(4월 3일자 3개월 CD금리), $$S(1)=231.7$$(4월 3일자 KOSPI 200 종가), $$dt= {1\over365}$$(365일간 변동한다고 가정)으로 설정한다.
- Z값을 일관성있게 정하기 위해 random seed는 3으로 설정한다.

# 2. MCS

위 식을 구현하는 매트랩 코드는 다음과 같다. 일단 volatility는 임의의 값인 0.3으로 설정하자. 예시일 뿐이므로 시뮬레이션을 실행하기 위한 for loop는 100번만 돌린다.

```(matlab)
clear; clf; randn('seed',3); hold;
S(1) = 231.7; r = 0.011; vol = 0.3;
T=1; N=365; dt=T/N;
Nt = datenum(2020,5,14)-datenum(2020,4,3)
t=linspace(0,dt*Nt,Nt+1);

for i=1:100
    Z=randn(1,Nt);
    for j=1:Nt
        S(j+1) = S(j) * exp(( r - 1/2 * vol^2 )...
        * dt + vol * Z( j ) * sqrt( dt ));
    end
    x(i) = S(end);
    plot(t, S, '-');
end
xlabel('time'); ylabel('KOSPI200');
mean(x)
```

그 결과 5월 14일 KOSPI200 지수의 기댓값은 228.0926로 계산된다. 이렇게 생성한 주가 경로를 플롯으로 그리면 다음과 같다.

![stock_process](https://github.com/cth127/cth127.github.io/blob/master/FEN101/stock_process.jpg?raw=true)

# 3. Implied Volatility

그럼 이제 본격적으로 call option의 implied volatility를 구해보자. volatility를 0.000에서 1.000사이 소숫점 2자리를 단위로 조정해가며 각각에 대해 10,000회 stock process를 진행하여 그 평균을 결과값으로 얻는다. 이에 대해 각 옵션의 strike price의 차를 구하여 payoff의 기댓값을 구하고, 이를 옵션의 시장가와 비교하여 MSE를 구한다. 비교 대상이 되는 5월 만기 KOSPI200 call option의 시장가는 다음과 같다.

|Strike Price|Market Price|
|---|---|---|
|255.0|2.79|
|252.5|3.50|
|250.0|4.00|
|247.5|4.96|
|245.0|5.68|
|242.5|6.83|
|240.0|7.60|
|237.5|9.00|
|235.0|10.20| 
|232.5|11.60|
|230.0|13.10|
|227.5|13.75|
|225.0|15.30|
|222.5|18.10|
|220.0|19.70|
|217.5|20.90|
|215.0|19.20|
|212.5|25.15|
|210.0|26.75|

그럼 코드를 구성해보자.

```(matlab)
clear; randn('seed',3);
S(1) = 231.7; r = 0.011;
T=1; N=365; dt=T/N;
Nt = datenum(2020,5,14)-datenum(2020,4,3);
t=linspace(0,dt*Nt,Nt+1);

X = linspace(210, 252.5, 18); %208~254 사이만
op=[26.75 25.15 19.20 20.90 19.70 18.10 15.30 13.75 13.10... 
    11.60 10.20 9.00 7.60 6.83 5.68 4.96 4.00 3.50];
vol=linspace(0, 1, 101);

for i=1:101
    for j=1:10000
        Z=randn(1,Nt);
        for k=1:Nt
            S(k+1) = S(k) * exp(( r - 1/2 * vol(i)^2 )...
            * dt + vol(i) * Z( k ) * sqrt( dt ));
        end
        res(j) = S(end);
    theory_price = max(mean(res) - X, 0) * exp(-r * dt * Nt); %현재가치로 할인
    mse(i) = mean((theory_price - op).^2);
    end
end

[argval argmin] = min(mse);
ans = vol(argmin)

% 그래프로 확인하기
clf;
plot(vol, mse, '-');
xlabel('Vol'); ylabel('MSE');
```
그 결과 MSE를 가장 작게 만드는 volatility 값은 0.74로 계산되었다. 다음은 Vol에 따른 MSE의 그래프이다.

![mse](https://github.com/cth127/cth127.github.io/blob/master/FEN101/mse_volume.jpg?raw=true)
