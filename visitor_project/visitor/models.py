from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    purpose = models.CharField(max_length=200)
    person_to_meet = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
