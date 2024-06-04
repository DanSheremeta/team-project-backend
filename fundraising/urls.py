from django.urls import path, include
from rest_framework import routers

from fundraising.views import FundraisingViewSet, LotViewSet

router = routers.DefaultRouter()
router.register("fundraising", FundraisingViewSet)
router.register("lot", LotViewSet)

urlpatterns = router.urls

app_name = "fundraising"
