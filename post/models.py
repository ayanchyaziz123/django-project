from django.db import models
from django import forms


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    postAuthor = models.CharField(max_length=200)
    postId = models.AutoField(primary_key=True, auto_created=True)
    postTitle = models.CharField(max_length=200)
    postTimeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    postText = models.TextField()
    postUrl = models.TextField(blank=True)
    postImage = models.ImageField(null=True, blank=True)

    def get_photo_url(self):
        if self.postImage and hasattr(self.postImage, 'url'):
            return self.postImage.url
        else:
            return "/static/aya.jpeg"

    def __str__(self):
        if len(self.postTitle) > 50:
            return self.postTitle[:50] + "..."
        else:
            return self.postTitle


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'postTitle', 'postText', 'postImage']
