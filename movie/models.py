from django.db import models

# Create your models here.
class Customer(models.Model):

    first = models.CharField(max_length=12)
    last = models.CharField(max_length=12)
    phonenumber = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first+" "+self.last

class Movie(models.Model):
    genre_choices =( ('Action', 'Action'),
                     ('Comedy', 'Comedy'),
                     ('Horror', 'Horror'),
                     ('Romentic', 'Romentic'),
                     ('Other', 'Other'), )

    moviename = models.CharField(max_length=30)
    releasedate = models.DateField(auto_now_add=False)
    genre = models.CharField(max_length=20 , choices=genre_choices)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    assigncustomer = models.ForeignKey('Customer' ,on_delete=models.SET_NULL,blank=True,null=True, )


    def __str__(self):
        return self.moviename