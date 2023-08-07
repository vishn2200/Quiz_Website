from django.db import models
from datetime import datetime

# Create your models here.
class careers(models.Model):
    career_title=models.CharField(max_length=200)
    career_content=models.TextField()
    career_published=models.DateTimeField('date published',default=datetime.now())

    def _str_(self):
        return self.career_title
class test(models.Model):
    Question=models.CharField(max_length=500)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    corrans=models.CharField(max_length=100)
    class Meta:
        db_table='test'
        
    
    
