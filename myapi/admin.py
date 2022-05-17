from django.contrib import admin
from .models import Alerts, AustralianArmy, British, CanadianArmy, IrregularMilitia, MiddleEasternAlliance, PanAsia, Post, Insurgent, RussianGroundForces, UnitedStatesArmy, UnitedStatesMarineCore
# Register your models here.
admin.site.register(Post)
admin.site.register(Alerts)
admin.site.register(British)
admin.site.register(Insurgent)
admin.site.register(AustralianArmy)
admin.site.register(CanadianArmy)
admin.site.register(IrregularMilitia)
admin.site.register(MiddleEasternAlliance)
admin.site.register(PanAsia)
admin.site.register(RussianGroundForces)
admin.site.register(UnitedStatesArmy)
admin.site.register(UnitedStatesMarineCore)