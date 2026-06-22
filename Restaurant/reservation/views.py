from django.shortcuts import render 
from .form import ReservationForm
# Create your views here.


def reserve(request):
    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
    if reserve_form.is_valid():
        reserve_form.save()
    else:
        reserve_form = ReservationForm()



    context = {
        'form':ReservationForm(request.POST)

}
    return render(request,'reservation/templates/reservation.html',context)
