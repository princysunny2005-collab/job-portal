from django.db import models

class RegisterModel(models.Model):
    profilepic =models.ImageField(upload_to="profile_image")
    fullname =models.CharField(max_length=50)
    email =models.EmailField()
    password =models.CharField()
    number =models.IntegerField()
    cv=models.FileField(upload_to="cariculam_vita")
