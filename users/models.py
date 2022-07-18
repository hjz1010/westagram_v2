from django.db import models

from utils.models import TimeStampModel

class User(TimeStampModel):
    email        = models.CharField(max_length=45)
    name         = models.CharField(max_length=45)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45)

    class Meta:
        db_table = 'users'

# class follow(models.Model):
#     follower  = models.ForeignKey(User, on_delete=models.CASCADE)
#     following = models.ForeignKey(User, on_delete=models.CASCADE) 

#     class Meta:
#         db_table = 'follows'
