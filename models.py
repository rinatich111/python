from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

#---------------------------------------------

from django.db import models

class Memeber(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

