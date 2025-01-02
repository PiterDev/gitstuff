from rest_framework import serializers

class RepoNameSerializer(serializers.Serializer):
    repo_name = serializers.CharField(max_length=255)
    repo_owner = serializers.CharField(max_length=255)