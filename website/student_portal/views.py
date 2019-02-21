from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . models import Personal
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . forms import UserForm
# Create your views here.


def login(request):
    return render(request, 'student_portal/login.html')


class IndexView(generic.list.ListView):
    context_object_name = "all_students"
    template_name = 'student_portal/list.html'

    def get_queryset(self):
        return Personal.objects.all()


class DetailView(generic.detail.DetailView):
    model = Personal
    context_object_name = "stud"
    template_name = 'student_portal/detail.html'

class PersonalCreate(CreateView):
    model = Personal
    fields = ['name','dept','regno']

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Personal.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)