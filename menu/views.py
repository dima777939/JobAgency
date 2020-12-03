from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import CreateView
from vacancy.models import Vacancy
from resume.models import Resume


class MenuView(View):
    mane_menu = {'login page': 'login', 'sign up page': 'signup', 'vacancies list': 'vacancies',
                 'resumes list': 'resumes', 'personal profile': 'home'}

    def get(self, request, *args, **kwargs):
        return render(request, "menu/menu.html", context={'mane_menu': self.mane_menu})


class MenuSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'http://127.0.0.1:8000/login'
    template_name = 'menu/signup.html'


class MenuLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/login.html'


class HomeForm(forms.Form):
    text = forms.CharField(max_length=1024)


class MenuCreatFormView(View):
    form_text = HomeForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                text_qs = Vacancy.objects.filter(author=request.user).values()
                text = [{'staff': 'vacancy'}]
            else:
                text_qs = Resume.objects.filter(author=request.user).values()
                text = [{'staff': 'resume'}]
            for i in text_qs:
                text.append({'description': i.get('description')})
            return render(request, 'menu/home.html', context={'context': text})
        return render(request, 'menu/menu_anonimus.html', context={'form': self.form_text})


class MenuCreatResumeVacancy(View):
    form_text = HomeForm

    def get(self, request, *args, **kwargs):
        return render(request, 'menu/form_creat_resume_vacancy.html', context={'form': self.form_text})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                Vacancy.objects.create(author=request.user, description=request.POST.get('text'))
                return redirect("/home/")
            Resume.objects.create(author=request.user, description=request.POST.get('text'))
            return redirect("/home/")
        return HttpResponseForbidden()