from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

#9h - 12h30 // 13h30 a 17h ++ 10min entre deux rendez-vous


class Appointment(models.Model):
    TIME_CHOICES = (
    ("9:00", "9:00"),
    ("9:30", "9:30"),
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True )
    date = models.DateTimeField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default ="9:00")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.name} | day: {self.date} | time: {self.time}"
    
