from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def profile (request) :
    return HttpResponse('Profile')


@login_required
def download (request, fileuuid) :
    return HttpResponse('Download')

