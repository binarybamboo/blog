from django.db import models
from users.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    post_num=models.IntegerField(default=0,null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=True)

    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)

    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

    def get_markdown_content(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    text = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_markdown_content(self):
        return markdown(self.text)

    def get_absolute_url(self):
        return self.post.get_absolute_url() + '#comment-id-{}'.format(self.pk)