from django.db import models

# Create your models here.


class regform(models.Model):
    name=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)
    experiance=models.CharField(max_length=225)
    linkdlnpro=models.CharField(max_length=225)
    jobcat=models.CharField(max_length=225)
    # resume=models.CharField(max_length=225)


class admin_login(models.Model):
    aname=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    passw=models.CharField(max_length=225)


class adregisterform(models.Model):
    afname=models.CharField(max_length=225)
    alname=models.CharField(max_length=225)
    aemail=models.CharField(max_length=225)
    passwd=models.CharField(max_length=225)
    cpasswd=models.CharField(max_length=225)



# class emp_login(models.Model):
#     aname=models.CharField(max_length=225)
#     email=models.CharField(max_length=225)
#     passw=models.CharField(max_length=225)









