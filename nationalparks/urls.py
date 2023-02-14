from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from parksapi.views import ParkView, WildlifeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'parks', ParkView, 'park')
router.register(r'wildlife', WildlifeView, 'wildlife')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
