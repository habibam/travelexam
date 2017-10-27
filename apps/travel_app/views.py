from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Trip

def index(request):
    # request.session.flush()
    if "first_name" not in request.session:
        return redirect('/')
    context = {
        'other_users': Trip.objects.exclude(id = request.session["id"]),
        'curr_user': User.objects.get(id=request.session['id']),
        'trips': Trip.objects.all()
    }

    return render(request, 'travel_app/index.html', context)
def add(request):
    if "first_name" not in request.session:
        return redirect('/')
    return render(request, 'travel_app/add.html')
def create(request):
    if "first_name" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    Trip.objects.create(destination = request.POST['destination'], description = request.POST['description'], travel_date_from = request.POST['travel_date_from'], travel_date_to = request.POST['travel_date_to'], plan_trip_id= user)
    return redirect('/travels')
def join(request, id):
    trip = Trip.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.plantrip.add(trip)
    return redirect ('/travels')
def remove(request, id):
    # user = User.objects.get(id = request.session["id"])
    Trip.objects.get(id=id).delete()
    return redirect("/travels")
def destination(request, id):
    context={
        'trip': Trip.objects.get(id=id),
    }
    return render(request, "travel_app/destination.html", context)
# Create your views here.
