from django.db import models

# Create your models here.
from django.db import models


class News(models.Model):
    news_text = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title

