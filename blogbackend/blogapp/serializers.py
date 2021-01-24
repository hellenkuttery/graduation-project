from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    model=Post
    fields=["title","author","content"]