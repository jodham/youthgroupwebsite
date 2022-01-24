from django.http import *
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from .models import *
from django.contrib import messages
import json


# Create your views here.

def about(request):
    templatename = "about.html"
    context = {}
    return render(request, templatename, context)


@login_required(login_url='/login/')
def profile(request):
    templatename = "profile.html"
    Member = request.user
    context = {'Member': Member}
    return render(request, templatename, context)

# -----------------------------Listview------------------------


class MembersListView(ListView):
    model = member
    template_name = 'member_list.html'
    context_object_name = 'members'
    totalmembers = member.objects.all().count()
    context = {'totalmembers': totalmembers}
    ordering = ['-DateJoined']


class IndexView(ListView):
    model = Project
    template_name = 'index_list.html'
    context_object_name = 'projects'


class PostView(ListView):
    model = post
    template_name = 'post_list.html'
    context_object_name = 'mypost'
# -----------------------------Listview------------------------
# -----------------------------Updateview------------------------


# -----------------------------CreateView------------------------

class postCreateView(CreateView):
    model = post
    fields = ['description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# --------------------x---------CreateView---------x---------------
# -----------------------------DetailView------------------------


class MembersDetailView(DetailView):
    model = member
    template_name = 'member_detail.html'


class projectDetailView(DetailView):
    model = Project
    template_name = 'Project_detail.html'
# ----------------x-------------DetailView---------------x---------
# <-----------------------------register-section------------------------->


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        secondname = request.POST.get('secondname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        position = request.POST.get('position')
        primaryschool = request.POST.get('Primaryscool')
        highschool = request.POST.get('highschool')
        university = request.POST.get('university')
        password = request.POST.get('pass1')
        if member.objects.filter(username=username).exists():
            error = 'Username already exits'
            template_name = 'register.html'
            context = {"error": error}
            return render(request, template_name, context)
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = secondname
        user.save()
        Member = member()
        Member.firstname = firstname
        Member.secondname = secondname
        Member.username = username
        Member.email = email
        Member.position = position
        Member.Primaryscool = primaryschool
        Member.highschool = highschool
        Member.university = university
        Member.save()
        return redirect('index')
    if request.user.is_authenticated:
        return redirect('members')
    templatename = 'register.html'
    return render(request, templatename)


def enter(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('index')
    if not request.user.is_authenticated:
        error = "Wrong credentials"
        templatename = 'assets/login.html'
        context = {'error': error}
        return render(request, templatename, context)


def getout(request):
    logout(request)
    return redirect('index')


def validate(request):
    username = request.GET.get('username')
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
# <----------------x-------------register-section---------------x--------->
