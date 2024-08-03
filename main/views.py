from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import translation


class IndexView(View):

    def get(self, request):
        if request.LANGUAGE_CODE == 'ru':
            translation.activate(request.LANGUAGE_CODE)
        print(f'Current language code is {request.LANGUAGE_CODE}')
        return render(request, 'main/index.html')
