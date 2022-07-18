from django.db import models

from users.models import User
from utils.models import TimeStampModel

class Posting(TimeStampModel):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    image    = models.CharField(max_length=200)
    contents = models.TextField()

    class Meta:
        db_table = 'postings'

class Comment(TimeStampModel):
    posting  = models.ForeignKey(Posting, on_delete=models.CASCADE)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()

    class Meta:
        db_table = 'comments'

class Like(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    posting     = models.ForeignKey(Posting, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'
## ManyToMany로 바꿔보자아아아아아아아아아ㅏㅏㅏㅏ