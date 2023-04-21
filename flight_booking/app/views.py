from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Flight, Booking
from django.http import HttpResponse
from .forms import SignUpForm




def home(request):
    flights = Flight.objects.all()
    return render(request, 'home.html', {'flights': flights})


# @login_required
# def search_flights(request):
#     flights = Flight.objects.none() # initialize flights with an empty queryset
#     if request.method == 'POST':
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         flights = Flight.objects.filter(date=date, time=time)
#     if not flights:
#         message = "No flights available for the selected date and time."
#     else:
#         message = None
#     return render(request, 'searchflight.html', {'flights': flights})

@login_required
def search_flights(request):
  flights = Flight.objects.none()
  if request.method == 'POST':
    from_city = request.POST.get('from_city')
    to_city = request.POST.get('to_city')
    date = request.POST.get('date')
    time = request.POST.get('time')
    flights = Flight.objects.filter(from_city=from_city, to_city=to_city, date=date, time=time)
  return render(request, 'searchflight.html', {'flights': flights})
   
           

@login_required
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    if request.method == 'POST':
        # Check if seats are available
        if flight.seats_available() > 0:
            # Book the ticket
            booking = Booking.objects.create(flight=flight, user=request.user)
            return redirect('my_bookings')
        else:
            # Show error message
            return render(request, 'bookflight.html', {'flight': flight, 'error': 'No seats available.'})
    return render(request, 'bookflight.html', {'flight': flight})



@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'mybookings.html', {'bookings': bookings})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# def user_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})



def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



