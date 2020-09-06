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
    form.title = request.GET['title']
    form.name = request.GET['name']
    form.photo=request.GET['photo']
    form.explain = request.GET['explain']
    form.deal_method = request.GET['deal_method']
    form.deadline = request.GET['deadline']
    form.price = request.GET['price']
    form.location = request.GET['location']
    form.save()
    return redirect('/form/'+str(form.id))


