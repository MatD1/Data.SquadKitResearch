from django.db import models

# Create your models here.
class AustralianArmyWeapons(models.Model):
    Weapon = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='australian_army_weapons/')

    class Meta: 
        verbose_name_plural = "Australian Army Weapons"

    def __str__(self):
        return self.Weapon