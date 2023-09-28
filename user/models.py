from django.db import models

# Create your models here.
class contactus(models.Model):
     name=models.CharField(max_length=200,null=True)
     email=models.CharField(max_length=100,null=True)
     mobile=models.CharField(max_length=25,null=True)
     msg=models.TextField(null=True)
     def __str__(self):
         return self.name

class slider(models.Model):
     headlines=models.TextField()
     slider_dec=models.TextField()
     slider_picture=models.ImageField(upload_to='static/slider/',null=True)
     def __pict__(self):
          return self.headlines

class volunteer(models.Model):
     id=models.CharField(max_length=200,null=True)
     name=models.CharField(max_length=100,null=True)
     email=models.CharField(max_length=100,primary_key=True)
     mobile=models.CharField(max_length=30,null=True)
     city=models.CharField(max_length=50,null=True)
     current_position=models.CharField(max_length=100,null=True)
     picture=models.ImageField(upload_to='static/volunteer',null=True)
     def __str__(self):
          return self.name

class upcomingevents(models.Model):
     event_picture=models.ImageField(upload_to='static/upcomingevent/',null=True)
     event_title=models.CharField(max_length=200,null=True)
     event_details=models.TextField()
     event_date=models.DateField()
     event_place=models.CharField(max_length=300)
     event_purpose=models.CharField(max_length=300)
     def __str__(self):
          return self.event_title

class nhelp(models.Model):
     name=models.CharField(max_length=200,null=True)
     mobile=models.CharField(max_length=30,null=True)
     helptype=models.CharField(max_length=200,null=True)
     message=models.TextField(null=True)
     address=models.TextField(null=True)
     picture=models.ImageField(upload_to='static/picture',null=True)
     request_date=models.DateField()

class donateus(models.Model):
     name=models.CharField(max_length=200,null=True)
     picture=models.ImageField(upload_to='static/donator',null=True)
     mobile=models.CharField(max_length=30,null=True)
     email=models.CharField(max_length=200,null=True)
     city=models.CharField(max_length=100,null=True)
     address=models.TextField()
     pincode=models.CharField(max_length=15,null=True)
     rupees=models.IntegerField(null=True)
     ddate=models.DateField(null=True)

class schange(models.Model):
     title=models.CharField(max_length=300,null=True)
     picture=models.ImageField(upload_to='static/pic',null=True)
     description=models.TextField(null=True)