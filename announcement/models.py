from django.db import models
from django.conf import settings
from courses.models import courseName
from django.utils import timezone
from django.contrib.auth.models import Permission, User


class Announcement(models.Model):
    courseName = models.ForeignKey(courseName, on_delete=models.CASCADE)
    User = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='announcements/',default="/default/announce.jpeg")
    at = models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #   return self.title

    def get_absolute_url(self):
        return "/Announcement/detail/%s/" % (self.id)

    def delete_url(self):
        return "/Announcement/delete/%s" % (self.id)

    def update_url(self):
        return "/courses/update/%s" % (self.id)
    def redirect(self):
        return "/courses/view/%s" % (self.courseName.name)



class comment(models.Model):
    Announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    text = models.TextField()
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Announcement.courseName.name
