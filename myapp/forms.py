from cProfile import label
from operator import attrgetter
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Posts,UserProfile

from django import forms

class RegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="Username")

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Confirm Password")

    class Meta:
        model=User
        fields=[
            "first_name","last_name","username","email","password1","password2",
        ]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
        }
        labels={
            "first_name":"First Name",
            "last_name":"Last Name",
            "username":"Username",
            "email":"Email",
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="Username")
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Password")
    class Meta:
        model=User
        fields=["username",
                "password"]
        widgets={
                "username":forms.TextInput(attrs={"class":"form-control"}),

        }
    

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["image","post"]
        widgets={
            "image":forms.FileInput(attrs={"class":"form-select"}),
            "post":forms.Textarea(attrs={"class":"form-control","rows":3}),
            
        }
        labels={
            "image":"Image",
            "post":"Description",
            
        }
class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=["address","dob","pro_pic","gender"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control","rows":2}),
            "dob":forms.DateInput(attrs={"class":"form-control"}),
            "pro_pic":forms.FileInput(attrs={"class":"form-control"}),
            "gender":forms.TextInput(attrs={"class":"form-control"}),
        }
        labels={
            "address":"Address",
            "dob":"DOB",
            "pro_pic":"Profile Picture",
            "gender":"Gender",
        }