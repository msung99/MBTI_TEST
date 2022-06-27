from .models import Comment
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogForm, BlogModelForm, CommentForm, Blog
from django.utils import timezone
from accounts.models import myUser

# Create your views here.

def home(request):
    return render(request, 'index.html')

def community(request):
    #블로그 글들을 모두 띄우는 코드 db에서 블로그 글들을 모두 가져와야함
    #posts = Blog.objects.all() #블로그라는 객체를 모두 가져올거다
    posts = Blog.objects.filter().order_by('-date')
    return render(request,'community.html',{'posts': posts})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        comment = Comment()
        comment.comment = filled_form.cleaned_data['comment']
        comment.post = get_object_or_404(Blog, pk = blog_id)
        comment.post2 = get_object_or_404(myUser, pk = request.user.id)
        comment.save()
        
    return redirect('detail', blog_id) #이런 blog_id를 prefix로 갖고있는 detail페이지로 이동하겠다

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 detali.html로 띄어주는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    #Blog객체를 한 개를 가져올건데 pk값이 blog_id 값인 객체를 가져올것 
    comment_form = CommentForm()
    user_id = request.user.id
    
    
    return render(request, 'detail.html',{'blog_detail':blog_detail,'comment_form':comment_form})


def formcreate(request):
    if(request.method == 'POST'):
        form = BlogForm(request.POST)
        if(form.is_valid()):
            post = Blog()
            user_id = request.user.id
            post.writer = get_object_or_404(myUser, pk = user_id)
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('community')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form': form})

def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            posts = Blog.objects.filter().order_by('-date')
            return render(request,'community.html',{'posts': posts})
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

def delete_board(request, board_id):
    board = Blog.objects.get(pk = board_id)
    board.delete()
    return redirect('community')

def delete_comment(request, blog_id, comment_id):
    comment = Comment.objects.get(pk = comment_id)
    comment.delete()
    return redirect('detail', blog_id)


def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)

    if(request.method == 'POST'):   
        form = BlogModelForm(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.date = timezone.now()
            blog.save()
            return redirect('detail', blog_id)
    else:
        form = BlogModelForm(instance = blog)
        return render(request, 'update.html', {'form' : form})


# def update_comment(request, blog_id, comment_id):
#     comment = get_object_or_404(Comment, pk = comment_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment.comment = form.cleaned_data['comment']
#             comment.save()
#             return redirect('detail', blog_id)
#     else:
#         form = CommentForm()
#         return render(request, 'update_comment.html', {'form':form})

def update_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id )
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm(instance = comment)
        return render(request, 'update_comment.html', {'form' : form})