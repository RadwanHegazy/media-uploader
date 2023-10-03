from django.shortcuts import render, HttpResponse



def login (request) : 
    return HttpResponse('login')

def register (request) : 
    return HttpResponse('register')