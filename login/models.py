from django.db import models

# Create your models here.
# After each edit run this = python manage.py makemigrations login
# and then this = python manage.py migrate

class User(models.Model):
    user = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    profilePic = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)        #uses the primary key asssigned to each user and imports it as a ForeignKey into the Property table. When a user is deleted the Propert associated is also deleted!
    #INSERT MORE COLUMNS!
