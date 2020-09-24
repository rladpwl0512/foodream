from django.shortcuts import render,get_object_or_404, redirect
from upload.models import Form

# Create your views here.
def home(request):
    forms = Form.objects
    count = Form.objects.count()
    return render(request, 'home.html', {'context' : count, 'forms': forms})

# def detail(request, form_id):
#     form_detail =get_object_or_404(Form, pk = form_id)
#     return render(request, 'detail.html', {'form': form_detail})