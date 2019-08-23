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