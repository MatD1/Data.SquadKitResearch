from datetime import datetime
from tabnanny import verbose
import uuid
from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    createdat = models.DateTimeField(datetime.now, auto_now=True)

    class Meta:
      verbose_name_plural = "Posts"

    def __str__(self):
        return self.name

class Changelog(models.Model):
    UpdateName = models.CharField(max_length=50, verbose_name='Changelog Name')
    body = models.TextField(verbose_name='Changelog details')
    createdat = models.DateTimeField(datetime.now, auto_now=True)

    class Meta:
      verbose_name_plural = "Changelogs"

    def __str__(self):
        return self.UpdateName
        
class Alerts(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=600)
    createdAt = models.DateTimeField(datetime.now, auto_now=True)

    class Meta:
      verbose_name_plural = "Alerts"

    def __str__(self):
        return self.name

class AustralianArmy(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    UUID = models.UUIDField(default=uuid.uuid4, editable=False )
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Australian Army"

    def __str__(self):
        return self.RoleName

class CanadianArmy(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Canadian Army"

    def __str__(self):
        return self.RoleName

class IrregularMilitia(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Irregular Militia"

    def __str__(self):
        return self.RoleName

class MiddleEasternAlliance(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Middle Eastern Alliance"

    def __str__(self):
        return self.RoleName

class PanAsia(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Pan-Asia"

    def __str__(self):
        return self.RoleName

class RussianGroundForces(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Russian Ground Forces"

    def __str__(self):
        return self.RoleName

class UnitedStatesArmy(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot', unique=True)
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "United States Army"

    def __str__(self):
        return self.RoleName

class UnitedStatesMarineCore(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "United States Marine Core"

    def __str__(self):
        return self.RoleName

class Insurgent(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    hasPrimary2 = models.BooleanField(default=False, verbose_name='Has Primary Weapon 2', help_text='Does the role have a second primary weapon?')
    PrimaryWeapon = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeapon_2 = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon #2')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    Primary_2_MagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount #2')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    Primary_2_MagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount #2')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "Insurgents"

    def __str__(self):
        return self.RoleName

class British(models.Model):
    RoleName = models.CharField(max_length=60, default='N/A', verbose_name='Role Name', unique=True)
    faction = models.CharField(max_length=35, default='N/A', verbose_name='Role Faction')
    isLeadOrCommand = models.BooleanField(default=False, verbose_name='Is Role Lead or Command?')
    isFireSupport = models.BooleanField(default=False, verbose_name='Is Role Fire Support?')
    isSpecialst = models.BooleanField(default=False, verbose_name='Is Role Specialst?')
    isSquadRole = models.BooleanField(default=False, verbose_name='Is Regular Squad Role?')
    PrimaryWeapon = models.CharField(max_length=40, default='N/A', verbose_name='Role Primary Weapon')
    PrimaryWeaponSights = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Sight')
    PrimaryFiringModes = models.CharField(max_length=50, default='N/A', verbose_name='Role Primary Weapon Firing Modes')
    PrimaryMagazineAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')
    PrimaryMagazineRoundAmount = models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')
    SecondaryWeapon = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary')
    SecondaryWeaponSights = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Sights')
    SecondaryWeaponFiringModes = models.CharField(max_length=60, default='N/A', verbose_name='Role Secondary Weapon Firing Modes')
    SecondaryWeaponMagAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')
    SecondaryWeaponMagRoundAmount = models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')
    Knife = models.CharField(max_length=50, default='N/A', verbose_name='Role Knife')
  #Equipment Slot 3-6
    thirdSlot = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot')
    thirdSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot Amount' )
    thirdSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #2')
    thirdSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #2 Amount' )
    thirdSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #3')
    thirdSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #3 Amount' )
    thirdSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Third Equipment Slot #4')
    thirdSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Third Equipment Slot #4 Amount' )
    fourthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot')
    fourthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot Amount' )
    fourthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #2')
    fourthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #2 Amount' )
    fourthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Fourth Equipment Slot #3')
    fourthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Fourth Equipment Slot #3 Amount' )
    fifthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot')
    fifthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot Amount' )
    fifthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Fifth Equipment Slot #2')
    fifthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Fifth Equipment Slot #2 Amount' )
    sixthSlot = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot')
    sixthSlot_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot Amount' )
    sixthSlot_1 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #2')
    sixthSlot_1_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #2 Amount' )
    sixthSlot_2 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #3')
    sixthSlot_2_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #3 Amount' )
    sixthSlot_3 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #4')
    sixthSlot_3_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #4 Amount' )
    sixthSlot_4 = models.CharField(max_length=50, default='N/A', verbose_name='Sixth Equipment Slot #5')
    sixthSlot_4_Amount = models.PositiveIntegerField(default=0, verbose_name='Sixth Equipment Slot #5 Amount' )

    class Meta:
      verbose_name_plural = "British"

    def __str__(self):
        return self.RoleName