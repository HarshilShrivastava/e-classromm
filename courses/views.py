from django.shortcuts import render, get_object_or_404, redirect
from .models import courseName
from .forms import createcourse
from django.http import HttpResponseRedirect
from announcement.forms import AnnouncementForm
from announcement.models import Announcement
from django.contrib.auth.decorators import login_required
@login_required
def create(request):
    form = createcourse(request.POST, request.FILES)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()

        return HttpResponseRedirect("/accounts/profile")
    else:
        form = createcourse()
    return render(request, "add_course.html", {"form": form})

@login_required
def update(request, pk):
    instance = get_object_or_404(Announcement, pk=pk)
    form = AnnouncementForm(request.POST or None,request.FILES or None, instance=instance)
    obj1 = get_object_or_404(Announcement, pk=pk)
    a = obj1.courseName.name

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            
            instance.save()
            return HttpResponseRedirect("/courses/view/"+a)
        else:
            form = AnnouncementForm()
    return render(request, 'Announcement.html', {"form": form, "a": a,"instance":instance})

@login_required
def createannouncement(request, courseNam):
    form = AnnouncementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.User = request.user
        a = get_object_or_404(courseName, name=courseNam)
        instance.courseName = a
        form.save()
        return HttpResponseRedirect("/courses/view/"+a.name)

    else:
        form = AnnouncementForm()
    return render(request, 'Announcement.html', {"form": form})

@login_required
def join(request, courseNam):
    query = get_object_or_404(courseName, name=courseNam)
    query.joined_by = request.user
    query.save()
    return redirect("/courses/view/"+courseNam)

@login_required
def my_course(request, courseNam):
    qs1 = Announcement.objects.all().filter(courseName__name=courseNam)
    a = False
    qs = get_object_or_404(courseName, name=courseNam)

    if qs.created_by == request.user:
        a = True
    print(a)
    return render(request, "my_course.html", {"qs": qs1, "qs1": courseNam, "ab": a, "qw": qs})

@login_required
def allcourse(request):
    qs = courseName.objects.exclude(joined_by=request.user)
    return render(request, "allcourses.html", {"qs": qs})
