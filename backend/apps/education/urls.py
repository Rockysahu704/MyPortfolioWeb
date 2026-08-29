from django.urls import path

from .views import EducationViewSet


education_list = EducationViewSet.as_view({
    "get": "list",
})


urlpatterns = [

    path(
        "portfolio/<str:username>/education/",
        education_list,
        name="portfolio-education"
    ),

]