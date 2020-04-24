# Create your views here.
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PostSerializer,CommentSerializer,PostListSerializer,CategorySerializer
from .models import Post, Comment,Category

class PostView(APIView):
    def get(self, request, post_id, format=None):
        try:
            post = Post.objects.get(pk=post_id)
            post_serializer = PostSerializer(post)
            comments = Comment.objects.filter(post=post)
            comment_serializer = CommentSerializer(comments, many=True)
            return Response({
                'post': post_serializer.data,
                'comments': comment_serializer.data
            })
        except Post.DoesNotExist:
            return Response({"message": "post does not exist"}, status=status.HTTP_404_NOT_FOUND)

class PostListView(APIView):
    def get(self,request,page=1,format=None):
        posts = Post.objects.order_by('id')[(page - 1) * 10:page * 10]
        serializer=PostListSerializer(instance=posts,many=True)
        return Response(serializer.data)

class CategoryView(APIView):
    def get(self,request,format=None):
        categorys=Category.objects.order_by('-name')
        for category in categorys:
            post=Post.objects.filter(category=category)
            category.post_num=int(len(post))
        serializer=CategorySerializer(categorys,many=True)
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self,request,name,page=1, format=None):
        category=Category.objects.get(name=name)
        posts=Post.objects.order_by('id').filter(category=category)[(page - 1) * 10:page * 10]
        serializer=PostListSerializer(instance=posts, many=True)
        return Response(serializer.data)

