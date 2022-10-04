from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DsaUser(models.Model):
    user =  models.OneToOneField(User,on_delete = models.CASCADE)
    # todo other arguments
    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name_plural = 'DSA Users'
