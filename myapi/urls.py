from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet),
router.register(r'alerts', views.AlertsViewSet),
router.register(r'insurgents', views.InsurgentViewSet),
router.register(r'british', views.BritishViewSet),
router.register(r'australian-army', views.AustralianArmyViewSet),
router.register(r'canadian-army', views.CanadianArmyViewSet),
router.register(r'irregular-militia', views.IrregularMilitiaViewSet),
router.register(r'middle-eastern-alliance', views.MiddleEasternAllianceViewSet),
router.register(r'pan-asia', views.PanAsiaViewSet),
router.register(r'russian-ground-forces', views.RussianGroundForcesViewSet),
router.register(r'united-states-army', views.UnitedStatesArmyViewSet),
router.register(r'united-states-marine-core', views.UnitedStatesMarineCoreViewSet),

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]