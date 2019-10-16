from django.shortcuts import render, redirect
from .forms import AnnouncementForm, commentform
from courses.models import courseName
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import Permission, User
from .models import Announcement, comment



def detail(request, pk):
    obj = get_object_or_404(Announcement, pk=pk)
    ar = comment.objects.all().filter(Announcement=obj)
    print(ar.count())
    form = commentform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.by = request.user
        instance.Announcement = obj
        form.save()

    else:
        form = commentform()
    return render(request, 'Announcement_detail.html', {"obj": obj, "form": form, "ar": ar})


def dele(request, pk):

    obj = get_object_or_404(Announcement, pk=pk)

    a = obj.courseName.name
    Announcement.objects.filter(id=pk).delete()
    return redirect("/courses/view/"+a)
