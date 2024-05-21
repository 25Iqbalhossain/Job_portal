from django.db import models

class Comsingup(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=122)
    companyname=models.CharField(max_length=122)
    tradelicense = models.CharField(max_length=122)
    address = models.TextField(max_length=122)
    phone=models.CharField(max_length=14)
    city=models.CharField(max_length=122)

    def __str__(self):
        return self.email


class Comlogin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=122)

    def __str__(self):
        return self.email

class Candidatelogin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=122)

    def __str__(self):
        return self.email

class Candidatesingup(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    education = models.CharField(max_length=122)
    institution = models.TextField(max_length=122)
    phone = models.CharField(max_length=14)
    city = models.CharField(max_length=122)
    file=models.CharField(max_length=122)

    def __str__(self):
        return self.email