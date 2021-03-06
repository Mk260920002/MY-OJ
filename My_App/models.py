
from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User



class Problem(models.Model):
    name=models.CharField(max_length=50)
    problem_id=models.IntegerField(null=True)
    problem_desc=models.CharField(max_length=500)
    problem_defficulty=models.CharField(max_length=10)
    problem_status=models.CharField(max_length=10)
    problem_score=models.FloatField(null=True)

    def __str__(self):
      return self.name

class submissions(models.Model):
    problem=models.ForeignKey(Problem,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE, unique=False,null=False)
    submitted_at=datetime.now()
    Verdict=models.CharField(max_length=50,null=True)
    submitted_code=models.CharField( max_length=500,null=True)
    
    def __str__(self):
      return self.Verdict

class testcase(models.Model):
    problem=models.ForeignKey(Problem,on_delete=models.CASCADE)
    
    input=models.CharField(max_length=500)
    output=models.CharField(max_length=500)

    def __str__(self) :
        return self.problem.name

