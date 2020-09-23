from django.shortcuts import render, get_object_or_404, redirect
from .models import Mileage

# Create your views here.
def content(request, mileage_id):
    mileage_detail =get_object_or_404(Mileage, pk = mileage_id)
    return render(request, 'content.html',{'mileage': mileage_detail})


def donate(request, mileage_id):
    mileage = get_object_or_404(Mileage, pk = mileage_id)
    if(request.method == 'POST'):
        mileage.total_money =int(mileage.total_money) + int(request.POST.get('total_money'))
        mileage.save()
        return redirect('/mileage/' + str(mileage_id))


def popup(request):
    return render(request, 'popup.html')