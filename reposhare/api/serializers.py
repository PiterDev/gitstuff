from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["repo_name", "repo_description", "user_description", "published_date", "updated_date", "votes", "poster_id"]