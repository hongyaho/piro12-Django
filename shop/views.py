from django.shortcuts import render
from django.shortcuts import HttpResponse

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))
