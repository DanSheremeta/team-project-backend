from rest_framework import routers

from pet.views import PetViewSet, DescriptionViewSet

router = routers.DefaultRouter()
router.register("description", DescriptionViewSet)
router.register("pet", PetViewSet)

urlpatterns = router.urls

app_name = "pet"
