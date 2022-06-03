from django.db import models

class Reg(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    sid = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)

class Result(models.Model):
    coursecode = models.CharField(max_length=20)
    coursename = models.CharField(max_length=20)
    credit = models.CharField(max_length=20)
    result = models.CharField(max_length=20)

class Payment(models.Model):
    pinfo = models.CharField(max_length=20)
    ptype = models.CharField(max_length=20)
    date = models.DateField()
    ammount = models.CharField(max_length=20)


class Notice(models.Model):
    notice = models.TextField()
