# 05 - Django

### 1. 목표

* 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
* Python Web Framework를 통한 데이터 조작
* Object Relational Mapping에 대한 이해
* Template Variable을 활용한 Template 제작
* 영화 추천 사이트의 영화 정보 데이터 관리



### 2. 준비사항

1. **(필수)** Python Web Framework - Django

2. **(필수)** Python Web Framework 사용을 위한 환경 설정

   * 가상환경 Python 3.7

3. (선택) 샘플 영화 정보

   * 예시 영화 Input인 `data.csv` 가 있습니다.

4. 가상환경 설정

   ```bash
   # 가상환경 만들기
   $ python -m venv venv
   
   # 가상환경 실행
   $ activate
   (venv)
   
   $ git init
   Initialized empty Git repository in C:/Users/student/Desktop/genie/projects/project05/pjt05-django-project/.git/
   (venv)
   student@DESKTOP MINGW64 ~/Desktop/genie/projects/project05/pjt05-django-project (master)
   
   $ vi .gitignore
   (venv)
   
   # gitignore에 아래와 같이 추가해준다.
   # venv/
   # __pycache__
   # .vscode/
   ```

5. 장고 프로젝트 시작하기

   ```bash
   # django 설치 유무 확인
   $ pip list 
   
   # 없다면, 설치
   $ pip install django
   
   # 장고 프로젝트 지금 이 위치에 설치
   $ django-admin startproject pjt05 .
   
   # 서버 구동
   $ python manage.py runserver
   ```

6. app 생성

```bash
----=-----
app 생성
$ python manage.py startapp movies


settings.py 파일 설정

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

INSTALLED_APPS = [
    'movies',
    ..
]


---
url 정의
# pjt05/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]

# movies/urls.py
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),

]
--- 
view 정의
# movies/views.py


from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
    --- 
    
template정의
# movies/templates/movies/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>하이!</h1>
</body>
</html>


---
서버 실행해서 확인!


```



### 3. 요구사항

1. 데이터베이스

   * ORM을 통해 작성될 클래스 이름은 `Movie`이며, 다음 정보를 저장합니다.

   

   **Movie**

   | 필드명      | 자료형  | 설명              |
   | ----------- | ------- | ----------------- |
   | title       | String  | 영화명            |
   | title_en    | String  | 영화명(영문)      |
   | audience    | Integer | 누적 관객수       |
   | open_date   | Date    | 개봉일            |
   | genre       | String  | 장르              |
   | watch_grade | String  | 관람등급          |
   | score       | Float   | 평점              |
   | poster_url  | Text    | 포스터 이미지 URL |
   | description | Text    | 영화 소개         |

   

   1. `Movie 모델` 정의

   ```python
   # movies/models.py
   
   from django.db import models
   
   # Create your models here.
   class Movie(models.Model):
       title = models.CharField(max_length=20) # 영화명
       title_en = models.CharField(max_length=20) # 영문 영화명
       audience = models.IntegerField() # 누적관객수
       open_date = models.DateTimeField() # 개봉일
       genre = models.CharField(max_length=20) # 장르
       watch_grade = models.CharField(max_length=10) # 관람등급
       score = models.FloatField() # 평점
       poster_url = models.TextField() # 포스터 이미지 poster_url
       description = models.TextField() # 영화소개
   ```

   2. `makemigrations` (마이그레이션 파일 생성)

   ```bash
   $ python manage.py makemigrations
   Migrations for 'movies':
     movies\migrations\0001_initial.py
       - Create model Movie
   (venv)
   ```

   3. `migrate` (DB반영)

   ```bash
   $ python manage.py migrate
   Operations to perform:
   ```

   

2. **페이지**

   * base.html

     ```
     
     ```

     

   1. 영화목록

      ```
      from django.urls import path
      
      from . import views
      urlpatterns = [
          path('', views.index),
      
      ]
      
      #
      from django.shortcuts import render
      
      # Create your views here.
      def index(request):
          movies = Movie.objects.order_by('-id') # 최신글순
          context = {
              'movies': movies
          }
          return render(request, 'movies/index.html')
          
      ```

      ```html
      # index.html
      ```

      

### 데이터베이스 데이터입력

```shell
import csv
f = open('./../data.csv', 'r')
```



