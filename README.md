# Django

Django는 웹 어플리케이션을 프로젝트라고 부름

django-admin startproject (프로젝트이름)

python manage.py runserver

http://127.0.0.1:8000/ 접속 주소

C:\Users\김진산\Documents\workspace\django\mysite

Terminal : Ctrl + 'c' : runserver 종료

app 작은 서비스 단위

template : html 파일

1. settings에서 templates에 'DIRS':[BASE_DIR/''] 부분에 기본으로 되는 파일/폴더 지정

2. 어플 추가시 INSTALLED_APPS에 '어플이름' 추가해주기

3. urls 에 urlpattern 설정

4. urls에서 views에 함수로 이동

5. views에 정의된 함수로 페이지 이동

6. index에 이동할 태그 만들어 이동 페이지 경로 설정



>template --데이터 줘!--> view --쟤가 데이터 달래--> model --DB에서 데이터꺼내기--

>--data--> model --data--> view --data--> template 

### mathfilters를 이용하면  template연산도 가능하다!

>$ pip install django-mathfilters

사용할 template에  {% load mathfilters %} 입력 후 사용


- sub – subtraction 더하기

- mul – multiplication 곱하기

- div – division 나누기

- intdiv – integer (floor) division 정수나누기

- abs – absolute value 절대값

- mod – modulo 모듈러 연산

```Example:

{% load mathfilters %}

<h1>Basic math filters</h1>

<ul>
    <li>8 + 3 = {{ 8|add:3 }}</li>

    <li>13 - 17 = {{ 13|sub:17 }}</li>

    {% with answer=42 %}
    <li>42 * 0.5 = {{ answer|mul:0.5 }}</li>
    {% endwith %}

    {% with numerator=12 denominator=3 %}
    <li>12 / 3 = {{ numerator|div:denominator }}</li>
    {% endwith %}

    <li>|-13| = {{ -13|abs }}</li>
</ul>
```