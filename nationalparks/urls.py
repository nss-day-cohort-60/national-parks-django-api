"""nationalparks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))s
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from parksapi.views import ParkView, BlogView, WildlifeView, login_user, register_user, PhotoView, NaturalAttractionView, CampgroundView, EventView, AmenityView, FavoriteView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'parks', ParkView, 'park')
router.register(r'blogs', BlogView, 'blog')
router.register(r'wildlife', WildlifeView, 'wildlife')
router.register(r'photos', PhotoView, 'photo')
router.register(r'natural_attractions', NaturalAttractionView, 'natural_attraction')
router.register(r'campgrounds',CampgroundView, 'campgrounds')
router.register(r'events', EventView, 'events')
router.register(r'amenities', AmenityView, 'amenity')
router.register(r'favorites', FavoriteView, 'favorite')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
