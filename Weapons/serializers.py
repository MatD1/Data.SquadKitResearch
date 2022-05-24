from rest_framework import serializers

from Weapons.models import AustralianArmyWeapons


class AustralianArmyWeaponsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AustralianArmyWeapons
        fields = ['Weapon', 'description', 'image']