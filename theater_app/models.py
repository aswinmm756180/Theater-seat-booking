from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name="Is Admin")
    is_manager = models.BooleanField(default=False, verbose_name="Is Manager")
    is_user = models.BooleanField(default=False, verbose_name="Is User")


    def __str__(self):
        return self.username
    

class Movie(models.Model):
    name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies_managed')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Theater(models.Model):
    theater_name = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='theaters')
    location = models.TextField(max_length=255)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    manager_theater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='theaters_managed')
    time_slot_1 = models.TimeField(null=True, blank=True)
    time_slot_2 = models.TimeField(null=True, blank=True)
    time_slot_3 = models.TimeField(null=True, blank=True)
    time_slot_4 = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.theater_name



from django.db import models

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    booked = models.BooleanField(default=False)
    time_slot = models.CharField(max_length=20)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='seats')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_seats',null=True, blank=True)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_booked_seats',null=True, blank=True) 

    def __str__(self):
        return f"Seat {self.seat_number} ({self.time_slot}) - {'Booked' if self.booked else 'Available'}"
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    time_slot = models.CharField(max_length=20, null=True, blank=True)
    seats_booked = models.ManyToManyField(Seat, related_name='bookings', null=True, blank=True)
    booked_seat_numbers = models.CharField(max_length=255, null=True, blank=True)  # Field to store booked seat numbers
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.id} by {self.user.username}"



class Userchat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username} - {self.chat}"

 