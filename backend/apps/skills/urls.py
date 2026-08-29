from django.urls import path
from .views import SkillViewSet

skill_list = SkillViewSet.as_view({
    "get": "list",
})


urlpatterns = [

    path(
        "portfolio/<str:username>/skills/",
        skill_list,
        name="portfolio-skills"
    ),

]