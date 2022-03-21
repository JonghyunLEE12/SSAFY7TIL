# Computational Thinking

### 명제 ( 이진논리 )

- 참과 거짓을 객관적으로 판별 할 수 있는 문장
- p , q, r 로 표시
- 진리값 : 명제가 참 또는 거짓을 가지는 값

### 

### 논리

- 참과 거짓을 판별할 수 있는 법칙

- 명제 논리 : 명제 자체를 하나의 식으로
- 술어 논리 : ~ 이면, ~ 이다.



### 논리 연산자

- 단순한 명제를 연결 시켜주는 연산자
- 부정(NOT) : ~ 
- 논리합 ( OR ) : V
- 논리곱 ( AND ) : ^
- 배타적 논리합 ( XOR ) : ㊉
  - exclusive OR
- 조건 ( condition ) : ->
  - p -> q : p 이면 q 이다
- 쌍반조건( bicondition ) : <->
- etc : nand, nor



### 진리표 ( Truth table )

- 가능한 진리값을 모두 나열한 표



### " 조건이 거짓이면 , 결론은 항상 참 "

- 거짓을 가정하고 시작하면 결론은 항상 참



### 증명

- 연역법 : 주어진 사실이나 공리를 통해서 새로운 사실을 도출하는 방법
- 귀납법 : 관찰이나 실험에 기반한 가설에 대해 일반적인 규칙을 입증하는 방법

- 수학적 귀납법

  1. basis : n0 -> 성립

  2. hypothesis : n = k 성립한다고 가정

  3. step : n = k+1 -> 성립하는지 보이면 검증이 끝남

- 모순 증명법

  - p -> q 가 참일 때,
  - q 가 거짓이라고 가정하면 ,  p -> q 가 참이 되기 위해서는
    p 가 거짓이어야 한다.

- 대우 증명법

  -  p -> q 가 참이면 ~q -> ~p 가 참이다.



-----------



![image-20220321163536052](C:\Users\My\AppData\Roaming\Typora\typora-user-images\image-20220321163536052.png)

-> 진리표 그리면서 풀기

### 향등법칙

- 적어두기



### 교환 법칙

p v q <-> q v p

p ^ q <-> q ^ p



### 결합 법칙

( p v q) v r <-> p v ( q v r)



### 분배 법칙

p v ( q ^ r) <-> (p v q) ^ (p v r)



###  흡수 법칙

p v ( p ^ q ) <-> p



### 드모르간 의 법칙



~ ( p ^ q ) < -> ~ p v ~ q

~ ( p v q ) <-> ~ p ^ ~ q



---

![image-20220321170459364](C:\Users\My\AppData\Roaming\Typora\typora-user-images\image-20220321170459364.png)

A -> 모든 값

E -> 어떤 값



1-> 모든 실수 x 에 대해서  x^2 >= x 를 만족하는가?

​	=> 0.5 의 제곱은 더 작아지기 때문에 False





---



![image-20220321173033551](C:\Users\My\AppData\Roaming\Typora\typora-user-images\image-20220321173033551.png)

크기 비교는  A - B < 0 ==> A < B 형태로 풀자