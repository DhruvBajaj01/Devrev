from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search_flights/', views.search_flights, name='search_flights'),
    path('book_flight/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('login/', views.user_login, name='login'), 
    path('signup/', views.user_signup, name='signup'),
]
