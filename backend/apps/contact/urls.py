from django.urls import path

from .views import ContactMessageViewSet


contact_list = ContactMessageViewSet.as_view({
    "get": "list",
    "post": "create",
})


urlpatterns = [

    path(
        "portfolio/<str:username>/contact/",
        contact_list,
        name="portfolio-contact"
    ),

]