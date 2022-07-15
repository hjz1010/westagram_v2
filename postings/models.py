from django.db import models

from users.models import User
from utils.models import TimeStampModel

class Posting(TimeStampModel):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    image    = models.CharField(max_length=200)
    contents = models.TextField()

    class Meta:
        db_table = 'postings'