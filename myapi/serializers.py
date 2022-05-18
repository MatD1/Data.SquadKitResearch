from dataclasses import field
from rest_framework import serializers
from .models import Alerts, AustralianArmy, British, CanadianArmy, IrregularMilitia, MiddleEasternAlliance, PanAsia, Post, Insurgent, RussianGroundForces, UnitedStatesArmy, UnitedStatesMarineCore


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Posts"
        model = Post
        fields = ['id','name', 'body', 'createdat'];

class AlertsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Alerts
        fields = ['id','name', 'body', 'createdat'];
        
class InsurgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Insurgents"
        model = Insurgent
        fields = ['id','RoleName', 'hasPrimary2', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeapon_2', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'Primary_2_MagazineAmount', 'PrimaryMagazineRoundAmount', 'Primary_2_MagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class BritishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "British"
        model = British
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class AustralianArmySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Australian Army"
        model = AustralianArmy
        fields = ['uuid','id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']
        

class CanadianArmySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Canadian Army"
        model = CanadianArmy
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class IrregularMilitiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Irregular Militia"
        model = IrregularMilitia
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class MiddleEasterAllianceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Middle Eastern Alliance"
        model = MiddleEasternAlliance
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class PanAsiaSerializer(serializers.HyperlinkedModelSerializer):
    verbose_name_plural = "Pan Asia"
    class Meta: 
        model = PanAsia
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class RussianGroundForcesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "Russian Ground Forces"
        model = RussianGroundForces
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class UnitedStatesArmySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "United States Army"
        model = UnitedStatesArmy
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']

class UnitedStatesMarineCoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        verbose_name_plural = "United States Marine Core"
        model = UnitedStatesMarineCore
        fields = ['id','RoleName', 'faction', 'isLeadOrCommand', 'isFireSupport', 'isSpecialst', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife','thirdSlot', 'thirdSlot_Amount', 'thirdSlot_1', 'thirdSlot_1_Amount', 'thirdSlot_2', 'thirdSlot_2_Amount', 'thirdSlot_3', 'thirdSlot_3_Amount', 'fourthSlot', 'fourthSlot_Amount', 'fourthSlot_1', 'fourthSlot_1_Amount', 'fourthSlot_2', 'fourthSlot_2_Amount', 'fifthSlot', 'fifthSlot_Amount', 'fifthSlot_1', 'fifthSlot_1_Amount', 'sixthSlot', 'sixthSlot_Amount', 'sixthSlot_1', 'sixthSlot_1_Amount', 'sixthSlot_2', 'sixthSlot_2_Amount', 'sixthSlot_3', 'sixthSlot_3_Amount', 'sixthSlot_4', 'sixthSlot_4_Amount']