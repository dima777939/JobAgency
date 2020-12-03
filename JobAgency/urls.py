"""JobAgency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from menu.views import MenuView, MenuSignupView, MenuLoginView, MenuCreatFormView, MenuCreatResumeVacancy
from resume.views import ResumeMainView
from vacancy.views import VacancyMainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuView.as_view()),
    path('resumes/', ResumeMainView.as_view()),
    path('vacancies/', VacancyMainView.as_view()),
    path('signup/', MenuSignupView.as_view()),
    path('login/', MenuLoginView.as_view()),
    path('exit/', LogoutView.as_view()),
    path('home/', MenuCreatFormView.as_view()),
    path('vacancy/new/', MenuCreatResumeVacancy.as_view()),
    path('resume/new/', MenuCreatResumeVacancy.as_view()),
]
