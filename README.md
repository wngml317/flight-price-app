✈ Streamlit Flight Price Prediction 
========
<br>

> 이 앱은 streamlit을 사용하여 항공권의 가격 예측하는 프로젝트입니다. 좌석 클래스, 여행일까지 남은 일수, 소요시간 등의 데이터를 분석하여 항공권의 가격을 예측합니다. 또한 항공권 가격과의 상관계수를 나타내는 차트를 확인할 수 있습니다.   
> 머신러닝에 활용한 데이터셋은 'Ease My Trip' 웹사이트에서 제공한 2022년 2월 11일부터 3월 31일까지 수집된 항공권 예약 데이터입니다. 
>   > 📃 Dataset : https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction       


<br>
  
✔ Data Columns
-----
- airline : 항공사 이름, 6개의 다른 항공사
- flight : 비행 코드
- source_city : 항공편이 출발하는 도시, 6개의 고유한 도시
- departure_time : 출발 시간, 기간을 그룹화하여 생성 한 6개의 고유한 시간
- stops : 출발지와 목적지 도시 간의 경유지 수
- arrival_time : 도착 시간, 기간을 그룹화하여 생성한 6개의 고유한 시간
- destination_city : 목적지 도시, 항공편이 착륙할 6개의 고유한 도시
- class : 좌석 클래스, 비즈니스와 이코노미
- duration : 소요 시간, 도시 간 이동에 걸리는 전체 시간을 시간 단위로 표시  
- days_left : 여행일에서 예약일을 뺀 남은 일수
- price : 티켓 가격 정보



<!--
<br>
데이터 전처리
---------
### 예측할 때 사용한 컬럼
- 항공사 : One-Hot Encoding을 사용하여 문자열 값들을 숫자형으로 인코딩
- 경유지 수 
  * zero : 0
  * one : 1
  * two_or_more : 2
- 좌석 클래스 
  * Business : 1
  * Economy : 0
- 남은 일수 : 여행 날짜 - 오늘 날짜
- 소요시간 : 도착시간 - 출발시간
  * 출발 시간 : 사용자가 선택
  * 도착 시간 : 데이터셋에서 출발도시와 도착도시의 소요시간의 평균 구한 후, 출발 시간에서 더하여 자동으로 설정된다.


 
Transform후 ColumnTransformer에서 적용한 변수 순서를 맞춰준다.
-- >

<!--

✔ 항공권 예측
----
* 사용자가 이용할 항공권을 선택
* 출발지와 목적지 간의 경유지 수를 입력
* 좌석 클래스 (Economy, Business)를 선택
* 여행일을 선택하여 예약일로부터 남은 일수 구하기
* 출발 도시와 도착 도시를 선택
* 출발 시간을 선택하면 도착 시간은 자동으로 설정
* 예측 시작하기 버튼을 눌러 항공권 예측 시작
* 
### 예측할 때 활용하는 데이터
### 1. 출발지와 목적지 간의 경유지  수
### 2. 좌석 클래스 (Economy, Business)
### 3. 예약일로부터 여행일까지 남은 일수
### 4. 소요 시간
-->
  
    
<br>    

🛠 Tech
----
Language : 
```
Python
```
Development Environment : 
```
Colab, VSCode
```
Deploy : 
```
AWS, Streamlit
```

<br>


![predict](https://user-images.githubusercontent.com/70615959/172402805-42e89c90-d5a3-4e3e-8ced-d42e77b8b0c5.gif)
