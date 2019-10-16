from django.urls import path
from .views import create,   join,  my_course, createannouncement, allcourse,update
urlpatterns = [
    path('add/', create, name="add"),
    path("join/<str:courseNam>/", join, name="Join"),
    path('view/<str:courseNam>', my_course, name="courseprofile"),
    path("createAnnounce/<str:courseNam>", createannouncement, name="announce"),
    path("all/", allcourse, name="all"),
    path('update/<int:pk>', update, name="update"),
]
