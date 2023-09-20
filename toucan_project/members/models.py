from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.ManyToManyField(School)

    def __str__(self):
        return self.name
