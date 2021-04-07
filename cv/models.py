from django.db import models
# Create your models here.
class cv(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    # Address info
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.TextField()
    # Education info
    degreeName = models.CharField(max_length=200)
    university = models.CharField(max_length=200)

    #experience
    experience = models.CharField(max_length=1000,default='0')
    companyname = models.CharField(max_length=200, blank=True, null=True)


    # skills
    skills = models.TextField()
    shortBio = models.TextField()
    # project
    project = models.CharField(max_length=500,default = 'None')



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
