from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from django.contrib.auth.models import Permission, User


class courseName(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name="owner", on_delete=models.CASCADE)
    joined_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="joined")
    image = models.ImageField(blank=True, null=True, upload_to='courses/',default="/default/courses.jpeg")
    created_At = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/courses/view/%s" % (self.name)

    def join_url(self):
        return "/courses/join/%s" % (self.name)

    def get_url(request):
        return "/course/curse/%s" % (self.name)
