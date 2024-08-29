from django.db import models


# Create your models here.

class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    code = models.CharField(max_length=25)
    document = models.CharField(max_length=25)
    photo = models.CharField(max_length=200)
    number = models.CharField(max_length=25)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class User(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.email