from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


