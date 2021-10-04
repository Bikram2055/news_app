from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news_images/', blank=True)
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Videos(models.Model):
    link = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading
