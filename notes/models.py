from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def first_name(self):
        return self.author.first_name

    def last_name(self):
        return self.author.last_name

    def __str__(self) -> str:
        return self.title