from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE) #the Album class will not delete automatically while musician is deleted
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating=(
        (1,"worst"),
        (2, "bad"),
        (3, "good")
    )
    num_stars = models.IntegerField(choices=rating) #******************************************************************************
    def __str__(self):
        return self.name+", Rating "+ str(self.num_stars) #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&^^%%*****************************