from django.db import models

class TimeStampModel(models.Model):
    created_at   = models.DateTimeField(auto_now_add=True) 
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class User(TimeStampModel):
    email        = models.CharField(max_length=45)
    name         = models.CharField(max_length=45)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45)

    class Meta:
        db_table = 'users'