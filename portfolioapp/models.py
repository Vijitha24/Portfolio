from django.db import models

class Portfolio(models.Model):
    name= models.CharField(max_length=20)
    birthdate = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField(upload_to='profile_media')

    def __str__(self):
        return '{}'.format(self.name)

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='profile_media')

    def __str__(self):
        return '{}'.format(self.title)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_media')

    def __str__(self):
        return '{}'.format(self.title)

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.job_title)

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    graduation_year = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.degree)

class Certification(models.Model):
    title = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    date_issued = models.DateField()

    def __str__(self):
        return '{}'.format(self.title)

class Skill(models.Model):
    skill =  models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.skill )



