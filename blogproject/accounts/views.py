from django.shortcuts import redirect, render
from django.contrib import auth
from accounts.models import myUser 
from blogapp.models import Blog
# Create your views here.

from django.conf import settings
UserModel = settings.AUTH_USER_MODEL

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username = userid, password = pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('community')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        pwd2 = request.POST['confirm']
        nickname = request.POST['nickname']

        if pwd == pwd2:
            user = myUser.objects.create_user(username = userid, password = pwd, nickname = nickname)
            auth.login(request, user)
            return render(request, 'mbtitest.html')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def result(request):
    if request.method == 'POST':
        e = str(request.POST['E']) # '키' 값에 해당하는 value를 리턴해줌
        s = str(request.POST['S'])
        t = str(request.POST['T'])
        j = str(request.POST['J'])
        mbti = e+s+t+j
     # user = myUser.objects.create_user(username=userid,mbti=mbti)
   
       # user2 = myUser.objects.get(pk=myUser_id)
        user2 = myUser.objects.last()
        user2.mbti = mbti 
        user2.save()
    return render(request, 'result.html',{'user2':user2})


def community(request):
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'detail.html', {'posts', posts})

