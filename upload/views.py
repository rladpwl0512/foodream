from django.shortcuts import render,get_object_or_404, redirect
from .models import Form, Like
from django.utils import timezone
from django.core.paginator import Paginator





# Create your views here.


def upload(request):
    return render(request, 'upload.html')


def create(request):
    form = Form()
    form.title = request.POST.get('title')
    form.name = request.POST.get('name')
    form.photo=request.POST.get('photo')
    form.explain = request.POST.get('explain')
    form.deal_method = request.POST.get('deal_method')
    form.deadline = request.POST.get('deadline')
    form.price = request.POST.get('price')
    form.location = request.POST.get('location')
    form.save()
    return redirect('/form/'+str(form.id))


def detail(request, form_id):
    form_detail =get_object_or_404(Form, pk = form_id)
    return render(request, 'detail.html', {'form': form_detail})

# def detail(request, form_id):
#     current_user=request.user
#     current_form=Form.objects.get(pk=form_id)

#     if 'Like' in request.POST:
#         current_user_like=Like.objects.all().filter(user=current_user,form=current_form)
#         if current_user_like:
#             like=Like.objects.get(user=current_user, form=current_form)
#             if like.like:
#                 like.delete()
#                 current_form.like_count-=1
#             else:
#                 like.like=True
#                 like.save()
#                 current_form.like_count+=1
#             return render(request,'detail.html', {'current_form':current_form, 'current_user_like':current_user_like })
#         return render(request,'detail.html',{'current_form':current_form})    

def list(request):
      forms = Form.objects.all().order_by('-id')
      paginator = Paginator(forms,6)
      page = request.GET.get('page', 1)
      posts = paginator.get_page(page)
      return render(request, 'list.html',{'posts':posts})
