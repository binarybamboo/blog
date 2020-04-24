from rest_framework import serializers
from .models import Post, Comment,Category
from users.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('name','post_num')

class CommentSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField('%Y/%m/%d %H:%M:%S')
    modified_at = serializers.DateTimeField('%Y/%m/%d %H:%M:%S')
    post = serializers.CharField(source="post.get_absolute_url")
    author = serializers.CharField(source="author.get_full_name")
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author','text', 'created_at', 'modified_at')

class PostSerializer(serializers.ModelSerializer):
    created=serializers.DateTimeField('%Y/%m/%d %H:%M:%S') #created customize
    author=serializers.CharField(source="author.get_full_name")
    category = serializers.CharField(source="category.get_name",default='X') #시발 드디어..

    #author 은 forignkey라 따로 처리를 해줘야함 forignkey추가를 위해선 해당 연결된 모델을 serializer를 생성해줘야함

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created', 'author', 'category',)

class PostListSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField('%Y/%m/%d %H:%M:%S')
    author=serializers.CharField(source="author.get_full_name")
    category = serializers.CharField(source="category.get_name",default='X') #빈값을 serializer하면 오류가 뜨기떄문에 default값을 설정해줌.
    class Meta:
        model = Post
        fields = ('id', 'title', 'created', 'author', 'category', )
