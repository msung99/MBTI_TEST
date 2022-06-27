from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

    
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['title','body']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  #Comment라는 모델을 기반으로 입력값을 받을거다
        fields=['comment'] #이 부분만 입력받겠다는 의미
    
