from django.urls import path
from rest_framework import routers

from database.views import PetViewSet, DescriptionViewSet, LotViewSet

router = routers.DefaultRouter()
router.register("description", DescriptionViewSet)
router.register("pet_information", PetViewSet)
router.register("lot", LotViewSet)

urlpatterns = router.urls

app_name = "lots"
