from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

@api_view(["GET","POST"])
def post_list(request):
    if request.method =="GET":
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
        
    elif request.method=="POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Post is send"
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
