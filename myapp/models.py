from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class member(models.Model):
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class postdata(models.Model):
    datetime = models.DateTimeField(auto_now=True , blank=True )
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username