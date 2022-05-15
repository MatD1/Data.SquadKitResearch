from datetime import datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=30)
    body = models.TextField()
    createdat = models.DateTimeField(datetime.now)

    def __str__(self):
        return self.name
        
class Insurgent(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name')
    faction = models.CharField(max_length=20, default='N/A', verbose_name='Role Faction')
    PrimaryWeapon = models.CharField(max_length=30, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=30, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=30, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=30, default='N/A', verbose_name='Role Knife')

    def __str__(self):
        return self.RoleName

class British(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name')
    faction = models.CharField(max_length=20, default='N/A', verbose_name='Role Faction')
    PrimaryWeapon = models.CharField(max_length=40, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=30, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=30, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=30, default='N/A', verbose_name='Role Knife')

    def __str__(self):
        return self.RoleName