from django.db import models

class Account(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=150)

    def __str__(self):
        return  self.email 