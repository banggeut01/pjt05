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
   $ python manage.py startapp movies
   ```

   app을 설정한 후, `INSTALLED_APPS`에 반드시 등록해줘야 한다.

   1. `settings.py` 파일 설정

      ```python
      LANGUAGE_CODE = 'ko-kr'
      TIME_ZONE = 'Asia/Seoul'
      
      INSTALLED_APPS = [
          'movies',
          ..
      ]
      ```

   2. `url` 정의

      ```python
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
      ```

   3. `view` 정의

      ```python
      # movies/views.py
      
      from django.shortcuts import render
      
      # Create your views here.
      def index(request):
          return render(request, 'index.html')
      ```

   4. `template` 정의

      ```html
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
      ```

7. 서버 구동해서 확인

```bash
$ python manage.py runserver
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

   * `base.html`

     * 기본 템플릿
     *  웹사이트 내 모든 페이지에 확장되어 사용되는 가장 기본적인 템플릿
     
```html
     <!DOCTYPE html>
  <html lang="en">
     
  <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>게시판</title>
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
         integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
     </head>
     
     <body>
       <nav class="navbar navbar-expand-lg navbar-dark bg-info">
         <a class="navbar-brand" href="/movies/">홈</a>
         <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
           aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
         </button>
         <div class="collapse navbar-collapse" id="navbarNav">
           <ul class="navbar-nav">
             <li class="nav-item active">
               <a class="nav-link" href="https://movie.naver.com/" target="_blank">네이버 영화순위 보러가기<span class="sr-only">(current)</span></a>
             </li>
           </ul>
      </div>
       </nav>
       <div class="container mt-5">
         {% block body %}
      {% endblock %}
       </div>
       <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
         integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
       </script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
         integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
       </script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
         integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
       </script>
     </body>
     
     </html>
     ```
   
   
   
   1. 영화목록
   
      * 페이지 접근 URL `/movies/ `입니다.
      
      * 데이터베이스에 존재하는 모든 영화 목록이 표시되며, 각 영화의 `title`, `score`가 표시됩니다.
      
      * `title` 클릭 시, 해당 `영화 정보 조회` 페이지로 이동합니다.
      
      * `urls.py`
      
        ```python
        from django.urls import path
        
        from . import views
        urlpatterns = [
            path('', views.index),
        ]
        ```
      
      * `views.py`
      
        ```python
        from django.shortcuts import render
     from .models import Movie
        
        # Create your views here.
        def index(request):
         movies = Movie.objects.order_by('-id') # 최신글순
            context = {
                'movies': movies
            }
            return render(request, 'movies/index.html', context)
        ```
      
      * `index.html`
      
        ```html
        {% extends 'movies/base.html' %}
        {% block body %}
        <h1 class="text-center">영화 관리 페이지입니다.</h1>
        <a class="btn btn-primary mt-5" href="/movies/new/" role="button">영화 등록</a>
        <table class="table mt-5">
          <thead>
            <tr>
              <th scope="col">영화번호</th>
              <th scope="col">영화명</th>
              <th scope="col">평점</th>
            </tr>
          </thead>
          {% for movie in movies %}
          <tr>
            <th scope="row">{{ movie.id}}</th>
            <td>
              <a href="/movies/{{ movie.pk }}">
                {{ movie.title }}
              </a>
            </td>
              <td>{{ movie.score }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
        {% endblock %}
        ```
      
   2. 영화 정보 생성 Form
   
      * 해당 페이지에 접근하는 URL은 `/movies/new/` 입니다.
   
      * 영화 정보를 작성할 수 있는 Form이 표시됩니다.
   
      *  Form에 작성된 정보는 Form Submit 버튼 클릭 시 `영화 정보 생성` 페 이지로 생성 요청(request)과 함께 전송됩니다.
   
      * 요청 보내는 방식(method)  GET, POST 중 어느 것을 사용하여도 무관합니다.
   
      * `urls.py`
   
        ```python
        # ...
        path('new/', views.new),
        # ...
        ```
   
      * `views.py`
   
        ```python
        # ...
        def new(request):
            return render(request, 'movies/new.html')
        ```
   
      * `new.html`
   
        ```html
        {% extends 'movies/base.html' %}
        {% block body %}
        <h1>영화 등록하기</h1>
        <form action="/movies/create/" method="GET">
          <div class="form-group">
            <label for="exampleInputEmail1">영화명</label>
            <input type="text" class="form-control" id="exampleInputEmail1" placeholder="영화명을 입력하세요." name="title">
            <label for="exampleInputEmail2">영화명(영문)</label>
            <input type="text" class="form-control" id="exampleInputEmail2" placeholder="영문 영화명을 입력하세요." name="title_en">
            <label for="exampleInputEmail3">누적관객수</label>
            <input type="number" class="form-control" id="exampleInputEmail3" name="audience">
            <label for="exampleInputEmail4">개봉일</label>
            <input type="date" class="form-control" id="exampleInputEmail4" name="open_date">
            <label for="exampleInputEmail5">장르</label>
            <input type="text" class="form-control" id="exampleInputEmail5" name="genre">
            <label for="exampleInputEmail6">관람등급</label>
            <input type="text" class="form-control" id="exampleInputEmail6" name="watch_grade">
            <label for="exampleInputEmail7">평점</label>
            <input type="number" step=0.01 min="0.00" max="5.00" class="form-control" id="exampleInputEmail7" name="score">
            <label for="exampleInputEmail8">포스터 이미지 url</label>
            <input type="text" class="form-control" id="exampleInputEmail8" name="poster_url">
            <label for="exampleInputEmail9">영화 소개</label>
            <textarea class="form-control" id="exampleInputEmail9" name="description"></textarea>
          </div>
          <div>
            <button type="submit" class="btn btn-primary">영화 정보 등록!</button>
          </div>
        </form>
        {% endblock %}
        ```
   
   3. 영화 정보 생성
   
      * 해당 페이지에 접근하는 URL은` /movies/create/` 입니다.
   
      * 이전 페이지로부터 전송 받은 데이터를 데이터베이스에 저장합니다.
   
      * 해당 페이지에서 저장한 영화 정보를 조회하는 `영화 정보 조회` 페이지로 Redirect 합니다.
   
      * `urls.py`
   
        ```python
        # ...
        path('create/', views.create),
        # ...
        ```
   
      * `views.py`
   
        ```python
        # redirect 하기 위해 import하여줌
        from django.shortcuts import render, redirect
        
        # ...
        
        def create(request):
            title = request.GET.get('title')
            title_en = request.GET.get('title_en')
            audience = request.GET.get('audience')
            open_date = request.GET.get('open_date')
            genre = request.GET.get('genre')
            watch_grade = request.GET.get('watch_grade')
            score = request.GET.get('score')
            poster_url = request.GET.get('poster_url')
            description = request.GET.get('description')
            movie = Movie.objects.create(title=title, title_en=title_en, audience=audience, \
                 open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, \
                     poster_url=poster_url, description=description)
            # 영화 정보 조회 페이지
            return redirect(f'/movies/{movie.pk}/')
        ```
   
        
   
   4. 영화 정보 조회
   
      * 해당 페이지에 접근하는 URL은 `/movies/1/` , `/movies/2/` 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
   
      *  해당 Primary Key를 가진 영화의 **모든 정보**가 표시됩니다.
   
      *  영화 정보의 최하단에는 `목록` , `수정` , `삭제` 링크가 있으며, 클릭 시 각각 `영화 목록` ,` 해당 영화 정보 수정 Form` , `해당 영화 정보 삭제 페이지`로 이동합니다.
   
      * `urls.py`
   
        ```python
        # ...
        
        # movie_pk 동적으로 할당 
         path('<int:movie_pk>/', views.detail),
        # ...    
        ```
   
      * `views.py`
   
        ```PYTHON	
        # movie_pk(영화 정보 키를 받아옴)
        def detail(request, movie_pk):
            movie = Movie.objects.get(id=movie_pk)
            context = {
                'movie': movie
            }
            return render(request, 'movies/detail.html', context)
        ```
   
      * `detail.html`
   
        ```html
        {% extends 'movies/base.html' %}
        {% block body %}
        <h1 class="text-center">{{ movie.title }} 상세 보기</h1>
        <div>
          <img src="{{ movie.poster_url }}" alt="{{ movie.title }}포스터" style="max-width:50%;height:auto;">
          <table class="table mt-5">
            <tr>
              <td colspan="2">
                {{ movie.title }}
              </td>
            </tr>
            <tr>
              <td colspan="2" style="border-top:0px;">
                {{ movie.title_en }}
              </td>
            </tr>
            <tr>
              <td width="20%">평점</td>
              <td>{{ movie.score }}</td>
            </tr>
            <tr>
              <td>누적관객수</td>
              <td>{{ movie.audience }}</td>
            </tr>
            <tr>
              <td>개봉일</td>
              <td>{{ movie.open_date }}</td>
            </tr>
        
            <tr>
              <td>장르</td>
              <td>{{ movie.genre }}</td>
            </tr>
            <tr>
              <td>관람등급</td>
              <td>{{ movie.watch_grade }}</td>
            </tr>
            <tr>
              <td colspan="2">줄거리</td>
            </tr>
            <tr>
              <td colspan="2" style="border-top:0px;">{{ movie.description }}</td>
            </tr>
          </table>
        </div>
        <div>
            <!-- 목록, 수정, 삭제 버튼 -->
            <a class="btn btn-primary" href="/movies/" role="button">목록</a>
            <a class="btn btn-primary" href="/movies/{{ movie.pk }}/edit/" role="button">수정</a>
            <a class="btn btn-primary" href="/movies/{{ movie.pk }}/delete/" role="button">삭제</a>
        </div>
        {% endblock %}
        ```
   
   5. 영화 정보 수정 Form
   
      * 해당 페이지에 접근하는 URL은 `/movies/1/edit/` , `/movies/2/edit/` 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
   
      * 해당 Primary Key를 가진 영화 정보를 수정할 수 있는 Form이 표시 되며, 정보가 입력된 채로 영화 정보 생성에서와  같은 input들을 가지고 있습니다.
   
      * 요청을 보내는 방식(method)은 GET, POST 중 어느 것을 사용하여도 무관합니다.
   
      * `urls.py`
   
        ```python
        # ...
        path('<int:movie_pk>/edit/', views.edit),
        # ...
        ```
   
      * `views.py`
   
        ```python
        def edit(request, movie_pk):
            movie = Movie.objects.get(id=movie_pk)
            context = {
                'movie': movie
            }
            return render(request, 'movies/edit.html', context)
        ```
   
      * `edit.html`
   
        * 원래 있던 값 보여주기
          * `input`태그의 경우 `value`값 이용
          * `textarea` 태그의 경우 `<textarea>원래 있던 값</textarea>`이용
          * 개봉일의 경우 원래 있던 값이 보여지지 않는 문제가 있다.
            * '2019-03-04' 와 같이 입력돼야 보여짐 => 이 부분 차후 해결할 문제
   
        ```python
        {% extends 'movies/base.html' %}
        {% block body %}
        <h1>영화 수정하기</h1>
        <form action="/movies/{{ movie.pk }}/update/" method="GET">
          <div class="form-group">
            <label for="exampleInputEmail1">영화명</label>
            <input type="text" class="form-control" id="exampleInputEmail1" name="title" value="{{ movie.title }}">
            <label for="exampleInputEmail2">영화명(영문)</label>
            <input type="text" class="form-control" id="exampleInputEmail2" name="title_en" value="{{ movie.title_en }}">
            <label for="exampleInputEmail3">누적관객수</label>
            <input type="number" class="form-control" id="exampleInputEmail3" name="audience" value="{{ movie.audience }}">
            <label for="exampleInputEmail4">개봉일</label>
            <input type="date" class="form-control" id="exampleInputEmail4" name="open_date" value="{{ movie.date }}">
            <label for="exampleInputEmail5">장르</label>
            <input type="text" class="form-control" id="exampleInputEmail5" name="genre" value="{{ movie.genre }}">
            <label for="exampleInputEmail6">관람등급</label>
            <input type="text" class="form-control" id="exampleInputEmail6" name="watch_grade" value="{{ movie.watch_grade }}">
            <label for="exampleInputEmail7">평점</label>
            <input type="number" step=0.01 min="0.00" max="5.00" class="form-control" id="exampleInputEmail7" name="score" value="{{ movie.score }}">
            <label for="exampleInputEmail8">포스터 이미지 url</label>
            <input type="text" class="form-control" id="exampleInputEmail8" name="poster_url" value="{{ movie.poster_url }}">
            <label for="exampleInputEmail9">영화 소개</label>
            <textarea class="form-control" id="exampleInputEmail9" name="description">{{ movie.description }}</textarea>
          </div>
          <div>
            <button type="submit" class="btn btn-primary">영화 정보 수정!</button>
          </div>
        </form>
        {% endblock %}
        ```
   
        
   
   6. 영화 정보 수정
   
      * 해당 페이지에 접근하는 URL은 `/movies/1/update/` , `/movies/2/update/` 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
   
      *  해당 Primary Key를 가진 영화 정보를 이전 페이지로부터 전송 받은 데이터로 변경하여 데이터베이스에 저장합니다.
   
      * 해당 페이지에서 수정한 영화 정보를 조회하는 영화 정보 조회 페이지로 `Redirect` 합니다.
   
      * `urls.py`
   
        ```python
        # ...
        path('<int:movie_pk>/update/', views.update),
        # ...
        ```
   
      * `views.py`
   
        ```python
        def update(request, movie_pk):
            title = request.GET.get('title')
            title_en = request.GET.get('title_en')
            audience = request.GET.get('audience')
            open_date = request.GET.get('open_date')
            genre = request.GET.get('genre')
            watch_grade = request.GET.get('watch_grade')
            score = request.GET.get('score')
            poster_url = request.GET.get('poster_url')
            description = request.GET.get('description')
            movie = Movie.objects.get(pk=movie_pk)
            movie.title=title 
            movie.title_en=title_en
            movie.audience=audience
            movie.open_date=open_date
            movie.genre=genre
            movie.watch_grade=watch_grade
            movie.score=score
            movie.poster_url=poster_url
            movie.description=description
            movie.save()
            return redirect(f'/movies/{movie.pk}/')
        ```
   
   7. 영화 정보 삭제
   
      * 해당 페이지에 접근하는 URL은 `/movies/1/delete/` ,` /movies/2/delete/` 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으 로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
   
      * 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니 다.
   
      * `영화 정보 목록` 페이지로 Redirect 합니다.
   
      * `urls.py`
   
        ```python
        # ...
        path('<int:movie_pk>/delete/', views.delete),
        # ...
        ```
   
      * `views.py`
   
        ```python
        def delete(request, movie_pk):
            movie = Movie.objects.get(pk=movie_pk)
            movie.delete()
            return redirect('/movies/')
        ```
   
3. 향후 과제

   데이터베이스에 입력할 때, 일일히 값을 입력해주었지만

   [data.csv][./data.csv] 파일을 사용해 손쉽게 입력할 수 있도록 해야합니다.

