from django.urls import path

from .views import ProjectViewSet


project_list = ProjectViewSet.as_view({
    "get": "list",
})


urlpatterns = [

    path(
        "portfolio/<str:username>/projects/",
        project_list,
        name="portfolio-projects"
    ),

]