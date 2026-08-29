# from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import SocialMediaViewSet


# router = DefaultRouter()

social_list = SocialMediaViewSet.as_view({
    "get":"list",
})

# router.register(
#     "social",
#     SocialMediaViewSet,
#     basename="social"
# )

urlpatterns = [
    path(
        "portfolio/<str:username>/social/",
        social_list,
        name="portfolio-social"

    ),
    
]