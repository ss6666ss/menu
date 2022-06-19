from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.IntegerField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    dietary_fiber = models.FloatField(default=0)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return '<Menu:' + self.name + ', ' + str(self.calorie)
