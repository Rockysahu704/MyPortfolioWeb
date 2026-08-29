from rest_framework.routers import DefaultRouter

from .views import SocialMediaViewSet


router = DefaultRouter()

router.register(
    "social",
    SocialMediaViewSet,
    basename="social"
)

urlpatterns = router.urls