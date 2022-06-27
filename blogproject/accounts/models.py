from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class myUser(AbstractUser):
    nickname = models.CharField(max_length = 200)
    mbti = models.CharField(max_length = 15)
    