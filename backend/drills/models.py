from django.db import models
from ships.models import Ship
from users.models import User

# Create your models here.
class SafetyDrill(models.Model):

    DRILL_TYPES = (
        ("FIRE", "Fire Drill"),
        ("EVACUATION", "Evacuation"),
        ("MEDICAL", "Medical Emergency"),
    )

    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

    drill_type = models.CharField(
        max_length=50,
        choices=DRILL_TYPES
    )

    scheduled_date = models.DateField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.drill_type} - {self.ship.name}"
    
class DrillParticipation(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("ATTENDED", "Attended"),
        ("MISSED", "Missed"),
    )

    drill = models.ForeignKey(SafetyDrill, on_delete=models.CASCADE)

    crew_member = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    completion_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.crew_member.username} - {self.drill.drill_type}"