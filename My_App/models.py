from django.db import models
from django.contrib.auth.models import User
class submissions(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   url=models.URLField(blank=True)
   score=models.IntegerField(blank=True,null=True)

   def __str__(self):
       return self.user.username