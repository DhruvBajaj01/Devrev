from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    number = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField(default=60)
    from_city = models.CharField(max_length=100, default='Chennai')
    to_city = models.CharField(max_length=100, default='Kanpur')

    def __str__(self):
        return f'{self.number} - {self.date} - {self.time}'

    def seats_available(self):
        return self.seats - self.bookings.count()
    
    
class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.flight.number}'

class Meta:
    ordering = ['-timestamp']

