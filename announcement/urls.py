from django.urls import path
from . import views
urlpatterns = [

    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>/", views.dele)

]
