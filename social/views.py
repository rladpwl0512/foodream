from django.shortcuts import render

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return render(request, 'signin.html')
    
