---
title: "FEN101 - 03 Volatility Smile of KOSPI200 Call Option"
date: 2020-04-12
categories: FEN101 Pricing
use_math: true
---

# 1. Intro

[지난 글](https://cth127.github.io/fen101/pricing/FEN101-02-implied-volatility/)에서 우린 KOSPI200 Call Option의 이론가격을 구한 뒤, 시장가격과의 MSE를 구해 이를 최소화하는 하나의 Implied volatility를 계산하였다. 블랙숄즈 모델은 이처럼 자산 가격의 vol이 알려져있고, 상수(constant)라는 가정을 세우는데, 한편 시장에서 관찰되는 옵션의 vol은 행사가마다 다르게 계산되곤 한다. 

이를 우리는 그 형태에 따라 volatility smile, volatility smirk, 혹은 volatility frown라 부른다. 본 글에선 volatility smile의 기본적인 개념을 간단하게 소개하고, Matlab을 통해 옵션가와 이론가 사이의 MSE를 최소화하는 일차 방정식 형태의 volatility smile 구조를 구하고자 한다. 이때 MSE를 최소화하는 가장 정교한 값을 구하기 위해 머신러닝에서 주로 활용되는 경사하강법을 이용한다.

# 2. Volatility Smile

한 가지 염두해둬야 하는 사실이 있는데, 일반적으로 옵션의 가격은 vol값에 비례한다. 기초자산의 vol이 높아질 경우 콜옵션 소유자 입장에선 기초자산 가격이 급격하게 떨어져 deep out of the money 상태가 돼도 든 비용은 옵션을 살 때 지불한 옵션가격이 전부지만(이는 vol이 낮아 가격이 조금만 떨어져도 마찬가지이다) 급격히 올라 deep in the money 상태일 땐 가격의 상승분에 비례해 기대 이익이 높아진다. (이때는 vol이 낮아 가격이 조금만 오를 때보다 훨씬 높은 기대이익을 보인다) 즉 option pricing에 들어가는 다른 변수가 동일할 때 각 행사가에 따라 vol값이 높게 나타난다는 것은 그 옵션이 그만큼  높게 평가를 받는다는 것이고, 낮게 나타난다는 것은 그만큼 낮게 평가를 받는다는 것이다.

앞서 언급했듯이 Volatility Smile을 형태에 따라 smile, smirk 혹은 frown라 부른다. 각각은 기초자산에 따라, 상황에 따라 다르게 나타날 수 있다. 

![vol_smile](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Volatility_smile.svg/1024px-Volatility_smile.svg.png)

(출처는 [영문 위키](https://en.wikipedia.org/wiki/Volatility_smile). X축의 strike price는 절대가격이 아닌 spot price에 따른 상대가격이다.)

Volatility Smile은 주로 환율 옵션 시장에서 나타난다. 행사가가 현재가와 같거나 비슷할 때, 즉 at the money 상태일 때 vol은 가장 낮게 나타나며, 그 반대의 상태일 땐 높게 나타난다. 이러한 현상이 나타나는 이유는 단기적으로 환율 시장은 정규분포나 로그정규분포보다 꼬리가 두꺼운 fat-tail의 가격 분포를 보여왔기 때문이다. 즉 환율이 균형 상태에서 벗어나 지나치게 올라가거나 떨어질 경우, 정상화되는 경향을 보이는 다른 종류의 기초자산과는 달리, 더 극단적으로 올라가거나 떨어지는 모습을 보여왔기 때문이다. 

위의 설명과 섞어 말하자면, 환율이 정상적인 상황일 때를 염두한 옵션은 상대적으로 기대이익이 낮아 옵션도 낮게 평가되는 한편, 환율이 비정상적으로 올라가거나 내려가는 상황을 염두한 옵션은, 그 방향으로 환율이 더 이동하는 경향이 있기에 기대이익이 높아 옵션도 높게 평가되는 경향이 있는 것이다.

![vol_smirk](https://www.investopedia.com/thmb/uwFvxlO5AmddJtA3LdLj_1oFwqE=/1787x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/VolatilitySkew2-17197b230fb84ea9ae62955e956ffe0c.png)

(출처는 [Investopedia](https://www.investopedia.com/terms/v/volatility-skew.asp))

한편 Volatility Smirk(썩소)는 주로 주식 시장의 옵션에서 주로 나타나는 형태이다. 즉 주식 가격이 낮은 상황을 염두한 옵션은 높게 평가되는 경향이 있는 한편, 주식 가격이 높은 상황을 염두한 옵션은 낮게 평가되는 경향이 있다. 이러한 현상이 나타나는 이유는 주식 가격이 경험적으로 부적 왜도를 보이고 있기 때문이다.

![neg_skew](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Negative_and_positive_skew_diagrams_%28English%29.svg/669px-Negative_and_positive_skew_diagrams_%28English%29.svg.png)

(출처는 [영문 위키](https://en.wikipedia.org/wiki/Skewness))

즉 주식 가격이 급격히 올라가긴 어렵지만 급격히 떨어지긴 쉽다는 것이다. 이러한 현상이 벌어지는 이유로는 주로 두 가지가 지적되는데, 첫 번째는 시장의 레버리지로 인한 효과이다. 즉 주식 가격이 하락하면 회사나 금융기관의 부채비율이 증가하여 디폴트 위험이 증가하고, 이것이 악순환으로 이어져 변동상이 상승할 확률이 높아진다. 두 번째 이유는 붕괴 회피 성향(crashphobia)이다. 투자자들은 시장이 급격히 붕괴하는 상황에 대한 두려움을 가지고 있다. 이로 인해 일반적인 풋옵션보다 deep out of the money 상태에 있는 풋옵션이 상대적으로 높은 프리미엄을 보이는 현상도 나타나곤 한다.

![vol_frown](https://upload.wikimedia.org/wikipedia/commons/7/73/ConcaveDef.png)

(출처는 [영문위키](https://en.wikipedia.org/wiki/Concave_function))

Volatility Frown(울상)은 smile과 반대되는 형태로, 주로 기초자산이 어떤 이벤트를 앞두고 있고, 이로 인해 가격이 극단적으로 오르거나 내려갈 가능성이 공존하는 상황에서 나타난다. 예컨대 신약의 임상 실험을 기다리고 있다든지, 합병 발표가 나기 직전이라든지 하는 상황을 들 수 있다. 이러한 상황을 Price Jump라 한다. 

이로써 Volatility Smile에 대한 기본적인 내용을 알아보았다. 기억해야 할 사실은, 상황에 따라 다르긴 하지만 블랙숄즈모델의 가정과 달리, 옵션 가격은 행사가에 dependent하다는 것이다. 이제 지난 글에서 살펴보았던 KOSPI200 Call Option의 vol 구조를 일차방정식의 형태로 구해보도록 한다.

# 3. KOSPI200 Call Option

경사하강법은 비용함수값을 최소화하는 최적값을 아주 정교하게 찾을 수 있도록 도와주지만, 데이터의 구조가 복잡할수록, 그리고 다루는 변수가 많을수록 그래프에 local minimum이 발생하여 우리의 목표인 global minimum을 찾기 어렵게 만드는 경향이 있다. 따라서 초기값을 무엇으로 설정해야 하느냐에 대한 문제가 있다. 이를 해결하기 위해 우린 일차 방정식의 기울기와 절편값을 특정 범주 내로 설정한 뒤 조금씩 조정해가며 비용함수 그래프의 대략적인 형태를 구하고, global minimum을 형성하는 곳 근처에서 초깃값을 설정하여 경사하강법을 시행하는 것으로 한다.

우리가 목표로 하는 옵션의 행사가는 210-254 사이의 범주에 있고, vol은 퍼센트로 표시되므로 0-1 사이의 값을 가진다고 가정한다. 즉 다음과 같은 연립부등식이 성립한다.

$$ 0 \le 210a+b \le 1 $$

$$ 0 \le 254a+b \le 1 $$

이를 풀면 다음과 같은 범위를 얻을 수 있다.

$$ - {1 \over 44} \le a \le {1 \over 44} $$

$$ - {254 \over 44} \le b \le 1 + {254 \over 44}   \text{broadly, but dependent on 'a'} $$

그럼 이 사이 범위에서, 하지만 vol이 0-1 범위에서 넘어가지 않도록 조정해가며 비용함수 그래프의 모양을 파악해보도록 하자. 저번처럼 구간을 100개씩 나누고, 몬테카를로 시뮬레이션 실행수를 10000번으로 하면 너무 많으니 그 수를 1000으로 줄여서 시행한다.

```(matlab)
clear; randn('seed',3);
S(1) = 231.7; r = 0.011;
T=1; N=365; dt=T/N;
Nt = datenum(2020,5,14)-datenum(2020,4,3);
t = linspace(0,dt*Nt,Nt+1);

X = linspace(210, 252.5, 18); %208~254 사이만
op = [26.75 25.15 19.20 20.90 19.70 18.10 15.30 13.75 13.10... 
    11.60 10.20 9.00 7.60 6.83 5.68 4.96 4.00 3.50];

a = linspace(-1/44, 1/44, 51);
b = linspace(-254/44, 1+254/44, 51);

for i=1:101
    for j=1:101
        if 210*a(i) + b(j) >= 0 & 254*a(i) + b(j) >= 0 &...
           210*a(i) + b(j) <= 1 & 254*a(i) + b(j) <= 1 
            for k=1:18
                vol = X(k)*a(i) + b(j);
                for l=1:1000
                    Z=randn(1,Nt);
                    for m=1:Nt
                        S(m+1) = S(m) * exp(( r - 1/2 * vol^2 )...
                        * dt + vol * Z( m ) * sqrt( dt ));
                    end
                    res(l) = S(end);
                end
                theory_price = mean(max(res - X(k), 0)) * exp(-r * dt * Nt); %현재가치로 할인
                se(k) = (theory_price - op(k)).^2;
            end
            mse(i, j) = mean(se);
        else
            mse(i,j) = 299;
        end
    end
end

% mse 분포 그래프로 확인
clf;
hist(mse)
xlabel('Freq'); ylabel('MSE');
```

![mse_freq](https://github.com/cth127/cth127.github.io/blob/master/FEN101/mse_freq.jpg?raw=true)

mse의 분포를 포면 대부분의 값에서 if문을 충족시키지 못하는, 즉 vol 값이 0 이하이거나 1 이상이어서 지정된 299의 값을 받았다. 우리가 관심있을만한 값은 0-30 사이이다. 이를 나눠 등고선을 그려보면 다음과 같다.

```(matlab)
% a, b값에 따른 mse값 등고선 그래프로 확인
clf;
contourf(mse, [5, 10, 15, 20, 25, 30]);
xlabel('Slope Index'); ylabel('Intercept Index'); zlabel('MSE');
colorbar;

[argval_temp argmin_temp] = min(mse);
[argval argmin_j] = min(min(mse));
argmin_i = argmin_temp(argmin_j);
min_a = a(argmin_i)
min_b = b(argmin_j)
```

![mse_cont](https://github.com/cth127/cth127.github.io/blob/master/FEN101/mse_cont.jpg?raw=true)

확대한 그래프긴 하지만 가장 진한 파란색 값이 있는 부근에서 mse가 최소가 된다는 걸 알 수 있다. mse가 최소가 되는 값을 확인한 결과 a는 0, b는 0.3745로 확인되었다. 지난번에 구했던 상수 vol값인 0.37에 매우 근접한 값이다. 이제 이 점을 초기값으로 하여 경사하강법을 시행, 더 정교한 값을 얻어보자. 코딩의 편의를 위해 mse를 구하는 함수를 sigval이라는 함수로 저장하여 활용했다.

```(matlab)
function val=sigval(s)
randn('seed',3);
S(1) = 231.7; r = 0.011;
T=1; N=365; dt=T/N;
Nt = datenum(2020,5,14)-datenum(2020,4,3);
t=linspace(0,dt*Nt,Nt+1);

X = linspace(210, 252.5, 18); %208~254 사이만
op=[26.75 25.15 19.20 20.90 19.70 18.10 15.30 13.75 13.10... 
    11.60 10.20 9.00 7.60 6.83 5.68 4.96 4.00 3.50];
mat = X;
mat(2,:) = 1;
mat = transpose(mat);
vol = mat * s;

    for v=1:18
        for j=1:10000
            Z=randn(1,Nt);
            for k=1:Nt
                S(k+1) = S(k) * exp(( r - 1/2 * vol(v)^2 )...
                * dt + vol(v) * Z( k ) * sqrt( dt ));
            end
            res(j) = S(end);
        end
        theory_price = mean(max(res - X(v), 0)) * exp(-r * dt * Nt); %현재가치로 할인
        se(v) = (theory_price - op(v)).^2;
    end
    val = sqrt(mean(se));
end

clear; clf; hold on;
v(:,1) = [0 ; 0.3745];
da = 1.0e-6; db = 1.0e-4; rate = 1.0e-8; 
k=1; tol=1.0e-8; err=2*tol;

while err>tol
    mse(k) = sigval(v(:,k));
    v(1,k+1)=v(1,k)-rate*(sigval(v(:,k)+[da ; 0])-mse(k))/da;
    v(2,k+1)=v(2,k)-rate*(sigval(v(:,k)+[0 ; db])-mse(k))/db;
    err=abs(mean(v(:,k+1)-v(:,k)));
    k=k+1;
end

ans = v(:,end)
```

그 결과 mse는 1.0846에서 1.0839로 줄었지만, 눈에 띄는 차이는 보이지 않았다. 즉 작은 소수점 차이는 있었겠지만, 앞서 구한 a=0, b=0.3745 에서 크게 벗어나지 않았다. 즉 상수 vol에 가까운 것이다. 혹시 초기값의 문제인가 싶어 변수를 바꿔가벼 실험해보았으나 mse는 위 값에서 가장 작게 나타났다. 반복문이 돌아간 수 k 대 mse 그래프는 다음과 같았다.

![mse_final](https://github.com/cth127/cth127.github.io/blob/master/FEN101/final_mse.jpg?raw=true)

# 4. Outro

아쉽게도 앞서 설명한 volatility smile의 구조를 파악하는데는 실패했다. 하지만 데이터가 그렇다고 하니 조작을 할 수도 없는 노릇 아니겠는가?
