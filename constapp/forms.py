from django import forms
from .models import *


class supform(forms.Form):
    cname = forms.CharField(max_length=50)
    address=forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
class suplog(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
class matform(forms.Form):
    cname=forms.CharField(max_length=50)
    smat = forms.CharField(max_length=100)
    image=forms.ImageField()
    nmat = forms.CharField(max_length=50)
    quan = forms.IntegerField()
    per = forms.CharField(max_length=50)
    price = forms.IntegerField()
    des = forms.CharField(max_length=500)
class editproform(forms.Form):
    cname = forms.CharField(max_length=50)
    smat = forms.CharField(max_length=100)
    image = forms.ImageField()
    nmat = forms.CharField(max_length=50)
    quan = forms.IntegerField()
    per = forms.CharField(max_length=50)
    price = forms.IntegerField()
    des = forms.CharField(max_length=500)
class userform(forms.Form):
    fname=forms.CharField(max_length=50)
    email=forms.EmailField()
    address=forms.CharField(max_length=100)
    phone=forms.IntegerField()
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
class userlog(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
class buyform(forms.Form):


    nmat = forms.CharField(max_length=100)
    price = forms.IntegerField()
    quan = forms.IntegerField()
class finalform(forms.Form):
    nmat = forms.CharField(max_length=100)
    price = forms.IntegerField()
    quan = forms.IntegerField()
class macform(forms.ModelForm):
    class Meta:
        model = macmodel
        fields = '__all__'
class buynowform(forms.Form):
    cname = models.CharField(max_length=50)

    nmat = forms.CharField(max_length=100)
    price = forms.IntegerField()
    quan = forms.IntegerField()
class messageconfirmform(forms.Form):
    fname=forms.CharField(max_length=50)
    email=forms.EmailField()
    message=forms.CharField(max_length=500)
