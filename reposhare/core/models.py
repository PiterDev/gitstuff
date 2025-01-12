from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Repo(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('owner', 'name')

class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'repo')  # No duplicate votes
