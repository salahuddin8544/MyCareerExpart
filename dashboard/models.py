from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True )
    def __str__(self):
        return self.name

class HighestDegree(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True,unique=True )
    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True )
    def __str__(self):
        return self.name
class Specialization(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True )
    def __str__(self):
        return self.name
    
class SectorExperience(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True )
    def __str__(self):
        return self.name

class Company(models.Model): 
   avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
   name = models.CharField(max_length=250, null=True, blank=True)
   def __str__(self):
        return self.name
class JobType(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.name
class Job(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.ManyToManyField(JobType, null=True, blank=True)
    specializations = models.ManyToManyField(Specialization, null=True, blank=True)
    experience = models.IntegerField(max_length=25, null=True, blank=True)
    def __str__(self):
        return self.title


class CvTemplate(models.Model):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    resume = models.FileField(upload_to='avatars/', null=True, blank=True)
