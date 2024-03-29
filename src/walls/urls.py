"""kedja_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from .apps import WallsConfig
from . import views

app_name = WallsConfig.name


router = routers.DefaultRouter()
router.register(r'walls', views.WallListView)
router.register(r'walls', views.WallDetailView)
router.register(r'walls', views.WallUpdateDeleteView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls

