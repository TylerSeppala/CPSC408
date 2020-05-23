from django.forms import ModelForm
from .models import Post, PostFiles


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'genre', 'description']


class PostFilesForm(ModelForm):
    class Meta:
        model = PostFiles
        fields = ['demo', 'files', 'image']
