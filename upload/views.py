from django.shortcuts import render,get_object_or_404, redirect
from .models import Form


# Create your views here.
def detail(request, form_id):
    form_detail =get_object_or_404(Form, pk = form_id)
    return render(request, 'detail.html',{'form': form_detail})

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


