from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    TODAY_EXERCISE_CHOICESE = [
        ('쉬었어요', '쉬었어요'),
        ('하체', '하체'),
        ('팔', '팔'),
        ('등', '등'),
        ('복근', '복근'),
        ('가슴', '가슴'),
        ('어깨', '어깨'),
    ]
    today_exercise = models.CharField(
        max_length=5,
        choices=TODAY_EXERCISE_CHOICESE,
        default='쉬었어요',
    )