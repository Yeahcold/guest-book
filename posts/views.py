from django.shortcuts import render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가
from django.views.decorators.http import require_http_methods
from posts.models import *
from .serializer import PostSerializer

# Create your views here.

#APIview 사용 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# 게시글 목록
class PostList(APIView):
    def get(self, request, format = None) :
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request, format = None) :
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
# 단일 게시글
class PostDetail(APIView):
    # 게시글 하나 불러오기
    def get(self, request, id) :
        post = get_object_or_404(Post, id = id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    # 게시글 하나 수정하기
    def put(self, request, id):
        post = get_object_or_404(Post, id = id)
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid(): #update나 create는 역직렬화니까 유효성 검사 필요
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# 게시글 하나 삭제하기
class PostDelete(APIView) :
    def delete(self, request, id):
        password = request.data.get('password', None)
        if not password:
            return Response({"error": "비밀번호를 제공해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        post = get_object_or_404(Post, id=id)
        if post.password != password:
            return Response({"error": "비밀번호가 일치하지 않습니다."}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response({"deleted" : "게시글이 정상적으로 삭제되었습니다."}, status = status.HTTP_204_NO_CONTENT)

    

    


