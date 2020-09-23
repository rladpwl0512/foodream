from django.db import models

# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length =200)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ='images/', blank = True, null =True)
    explain = models.TextField()
    deal_method= models.CharField(max_length=200)
    deadline = models.ImageField(upload_to='images',null = True)
    price = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    like_count: models.IntegerField(default=0)


class Photo(models.Model):
    form = models.ForeignKey(Form, on_delete= models.CASCADE, null = True, related_name='form2')
    photo = models.ImageField(upload_to='images/', blank = True, null = True )
    

class Deadline(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, null = True, related_name ='form3')
    deadline= models.ImageField(upload_to='images/',null= True )




    

class Like(models.Model):    
    user = models. ForeignKey(User), on_delete=models.CASCADE, null = True)
    form = models. ForeignKey((Form, on_delete=models.CASCADE, null = True) 
    like = models. BooleanField       
