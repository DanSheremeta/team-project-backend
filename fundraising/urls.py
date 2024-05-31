from django.urls import path, include
from rest_framework import routers

from fundraising.views import FundraisingViewSet

router = routers.DefaultRouter()
router.register("fundraising", FundraisingViewSet)

urlpatterns = router.urls

app_name = "fundraising"
