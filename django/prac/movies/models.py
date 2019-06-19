from django.db import models

# Create your models here.

class Movie (models.Model):
    title= models.CharField(max_length=100)
    title_origin= models.CharField(max_length=100)
    vote_count= models.IntegerField()
    open_date= models.CharField(max_length=100)
    genre= models.CharField(max_length=100)
    score= models.FloatField()
    poster_url= models.TextField()
    description= models.TextField()

    def __str__(self):
        return f'제목:{self.title} 영화명:{self.title_origin} 투표수:{self.vote_count} ' \
            f'개봉일: {self.open_date} 장르: {self.genre} 점수:{self.score} 포스터:{self.poster_url} 설명: {self.description}'