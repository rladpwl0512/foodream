from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from upload.models import Form

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'로그인에 실패하였습니다.')
            return render(request, 'signin.html')

    #소셜로그인 성공할 시에 
    elif request.user.is_authenticated:
         return redirect('home')

    else:        
        return render(request, 'signin.html')