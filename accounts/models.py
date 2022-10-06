from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django import utils
# Create your models here.
class DsaUser(models.Model):
    user =  models.OneToOneField(User,on_delete = models.CASCADE)
    last_update_at = models.DateTimeField(default=utils.timezone.now())
    sheet_link = models.CharField(max_length=400,default='empty')

    # todo other arguments
    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name_plural = 'DSA Users'

class Topic(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=400,default='Untitled')
    difficulty = models.CharField(max_length=100,default = 'easy')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    link_to_problem = models.CharField(max_length=400,default="offline")
    notes = models.TextField()
    last_done_on = models.DateField()
    row_number = models.PositiveBigIntegerField(default = 1)
    topics = models.ManyToManyField(Topic)
    def __str__(self) -> str:
        return self.title