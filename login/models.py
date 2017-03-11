from django.db import models

# Create your models here.
# After each edit run this = python manage.py makemigrations login
# and then this = python manage.py migrate

class User(models.Model):
    # userID is auto Generated
    username = models.CharField(editable=False, max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)       # A CharField that checks that the value is a valid email address. It uses EmailValidator to validate the input.
    profilePic = models.URLField(max_length=1000)       # A CharField for a URL.

    def __str__(self):
        return self.username        # Returns the specific value as the value of the username

class Property(models.Model):
    # propertyID is auto Generated
    userID = models.ForeignKey(User, on_delete=models.CASCADE)        #uses the primary key asssigned to each user and imports it as a ForeignKey into the Property table. When a user is deleted the Propert associated is also deleted!
    assignedName = models.CharField(max_length=30)

    def __str__(self):
        return self.assignedName        # Returns the specific value as the value of the assignedName

class Address(models.Model):
    # addressID is auto Generated
    propertyID = models.ForeignKey(Property, on_delete=models.CASCADE)        # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    LineOne = models.CharField(max_length=50)
    LineTwo = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)

class Booking(models.Model):
    # bookingID is auto Generated
    propertyID = models.ForeignKey(Property, on_delete=models.CASCADE)      # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    guestID = models.ForeignKey(Property, on_delete=models.CASCADE)      # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    startDateTime = models.DateTimeField(auto_now=False, auto_now_add=False)        # A date and time, represented in Python by a datetime.datetime instance
    duration = models.DurationField()       # A field for storing periods of time - modeled in Python by timedelta. When used on PostgreSQL, the data type used is an interval and on Oracle the data type is INTERVAL DAY(9) TO SECOND(6).
    endDateTime = models.DateTimeField(auto_now=False, auto_now_add=False)        # A date and time, represented in Python by a datetime.datetime instance

class Guest(models.Model):
    # guestID is auto Generated
    bookingID = models.ForeignKey(Bookings, on_delete=models.CASCADE)       # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone = models.BigIntegerField(max_length=14)      # A 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.
    Email = models.EmailField(max_length=254)       # A CharField that checks that the value is a valid email address. It uses EmailValidator to validate the input.
    addressLineOne = models.CharField(max_length=50)
    addressLineTwo = models.CharField(max_length=50)
    addressCity = models.CharField(max_length=50)
    addressCountry = models.CharField(max_length=50)
