from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from parksapi.views import WildlifeView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'wildlife', WildlifeView, 'wildlife')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
