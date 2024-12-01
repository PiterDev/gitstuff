from django.db import models
import uuid

# Create your models here.

class Post(models.Model):
    repo_name = models.CharField(max_length=100)
    repo_description = models.TextField()
    user_description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField()
    poster_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.title