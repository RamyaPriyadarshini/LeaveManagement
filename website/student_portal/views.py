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

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'student_portal/login.html'

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         if user is not none:
#             if user.is_active:
#                 login(request, user)
#                 redirect(str(username))
#         return render(request, self.template_name, {'form': form})
