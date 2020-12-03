from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy


class VacancyMainView(View):

    def get(self, request, *args, **kwargs):
        data = Vacancy.objects.all()
        return render(request, 'vacancy/vacancy.html', context={'data': data})
