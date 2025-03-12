from django.db import models

# Create your models here.
class supreg(models.Model):
    cname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class matmodel(models.Model):
    catchoice=[
        ('CEMENT','CEMENT'),
        ('STEEL','STEEL'),
        ('METAL','METAL'),
        ('SAND','SAND'),
        ('BRICK','BRICK'),
        ('TOOLS','TOOLS')

    ]
    perchoice=[
        ('KG','KG'),
        ('SQUARE-FEET','SQUARE-FEET'),
        ('NUMBER','NUMBER'),
        ('HOUR','HOUR'),
        ('MINUTE','MINUTE')
    ]
    cname=models.CharField(max_length=50)
    smat=models.CharField(max_length=100,choices=catchoice)
    image=models.ImageField(upload_to='constapp/static')
    nmat=models.CharField(max_length=50)
    quan=models.IntegerField()
    per=models.CharField(max_length=50,choices=perchoice)
    price=models.IntegerField()
    des=models.CharField(max_length=500)

class userreg(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class buymodel(models.Model):

    nmat=models.CharField(max_length=100)
    price=models.IntegerField()
    quan=models.IntegerField()
class wishmodel(models.Model):
    catchoice=[
        ('CEMENT','CEMENT'),
        ('STEEL','STEEL'),
        ('METAL','METAL'),
        ('SAND','SAND'),
        ('BRICK','BRICK'),
        ('TOOLS','TOOLS')

    ]
    perchoice=[
        ('KG','KG'),
        ('SQUARE-FEET','SQUARE-FEET'),
        ('NUMBER','NUMBER'),
        ('HOUR','HOUR'),
        ('MINUTE','MINUTE')
    ]
    cname=models.CharField(max_length=50)
    smat=models.CharField(max_length=100,choices=catchoice)
    image=models.ImageField(upload_to='constapp/static')
    nmat=models.CharField(max_length=50)
    quan=models.IntegerField()
    per=models.CharField(max_length=50,choices=perchoice)
    price=models.IntegerField()
    des=models.CharField(max_length=500)
class macmodel(models.Model):
    perchoice=[
        ('HOUR','HOUR'),
        ('MINUTE','MINUTE')
    ]
    cname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='constapp/static')
    nmac=models.CharField(max_length=50)
    price=models.IntegerField()
    per=models.CharField(max_length=50,choices=perchoice)
    des=models.CharField(max_length=500)

class buynowmodel(models.Model):
    cname=models.CharField(max_length=50)
    nmat = models.CharField(max_length=100)
    price = models.IntegerField()
    quan = models.IntegerField()
class confirmmodel(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    message =models.CharField(max_length=500)

























