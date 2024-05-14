from django.urls import path
from rest_framework import routers

from app.views import Pet_informationViewSet, DescriptionViewSet

router = routers.DefaultRouter()
router.register("description", DescriptionViewSet)
router.register("pet_information", Pet_informationViewSet)

urlpatterns = router.urls
app_name = "app"
