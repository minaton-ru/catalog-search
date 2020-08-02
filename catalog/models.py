from django.db import models

class Car(models.Model):
    gearbox_mech = 1
    gearbox_auto = 2
    gearbox_robot = 3

    GEARBOX_CHOICES = [
        (gearbox_mech, "Механика"),
        (gearbox_auto, "Автомат"),
        (gearbox_robot, "Робот"),
    ]
    manufacturer = models.CharField(max_length=128)
    model = models.CharField(max_length=56)
    year = models.IntegerField()
    gearbox = models.SmallIntegerField(choices=GEARBOX_CHOICES, default=gearbox_auto)
    color = models.CharField(max_length=128)

    def __str__(self):
	    return self.manufacturer + ' ' + self.model


