from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.IntegerField()
    litr = models.IntegerField()
    batafsil = models.TextField()

    def __str__(self):
        return self.brend


class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=50)
    qarz = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.IntegerField()
    ish_vaqti = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin - {self.ism}"

class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    kiritilgan_sana = models.DateField()

    def __str__(self):
        return f"Haydovchi - {self.ism}"

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv,on_delete=models.CASCADE)
    kiritilgan_sana = models.DateField()
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    umumiy_narx = models.IntegerField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi,on_delete=models.CASCADE)


