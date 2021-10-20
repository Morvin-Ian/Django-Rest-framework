from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    Adm_no = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name

