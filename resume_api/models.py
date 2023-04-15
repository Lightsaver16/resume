from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=50)


class Education(models.Model):
    university_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=100)
    university_address = models.CharField(max_length=200)


class Skills(models.Model):
    name = models.CharField(max_length=50)
