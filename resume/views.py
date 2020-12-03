from django.shortcuts import render
from django.views.generic.base import View
from resume.models import Resume , User


class ResumeMainView(View):

    def get(self, request, *args, **kwargs):
        data = Resume.objects.all()
        return render(request, 'resume/resume.html', context={'data': data})
