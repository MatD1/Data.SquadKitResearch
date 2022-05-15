from dataclasses import field
from rest_framework import serializers
from .models import British, Post, Insurgent


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Post
        fields = ['id','name', 'body', 'createdat'];
        
class InsurgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Insurgent
        fields = ['id','RoleName', 'faction', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife']

class BritishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = British
        fields = ['id','RoleName', 'faction', 'PrimaryWeapon', 'PrimaryWeaponSights', 'PrimaryFiringModes', 'PrimaryMagazineAmount', 'PrimaryMagazineRoundAmount', 'SecondaryWeapon', 'SecondaryWeaponSights', 'SecondaryWeaponFiringModes', 'SecondaryWeaponMagAmount', 'SecondaryWeaponMagRoundAmount', 'Knife']
        