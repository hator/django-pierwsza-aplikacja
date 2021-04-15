from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
