from django.urls import path

from .views import ExperienceViewSet


experience_list = ExperienceViewSet.as_view({
    "get": "list",
})


urlpatterns = [

    path(
        "portfolio/<str:username>/experience/",
        experience_list,
        name="portfolio-experience"
    ),

]