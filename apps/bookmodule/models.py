from django.db import models

# Create your models here.
class Publisher(models.Model):
 name = models.CharField(max_length=200)
 location = models.CharField(max_length=300)
 def __str__(self):
        return self.name

class Author(models.Model):
 name = models.CharField(max_length=200)
 DOB = models.DateField(null=True)
 def __str__(self):
        return self.name

class Book(models.Model):
 title = models.CharField(max_length= 100)
 price = models.FloatField(default=0.0)
 quantity = models.IntegerField(default=1)
 pubdate = models.DateTimeField()
 rating = models.SmallIntegerField(default = 1)


 publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
 authors = models.ManyToManyField(Author)

 
class Address(models.Model):
    city = models.CharField(max_length= 100)
    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length= 100)
    age = models.IntegerField()
    address = models.ManyToManyField(Address)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length= 100)
    image = models.FileField(upload_to='docs/') 
    def __str__(self):
        return self.name
