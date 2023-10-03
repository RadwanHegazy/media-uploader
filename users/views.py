from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth.views import auth_login

def login (request) : 
    context = {}

    if request.method == "POST" : 

        try : 
            data = {
                'email' : request.POST.get('email'),
                'password' : request.POST.get('password'),
            }
            
            u = User.login(**data)

            print(u)
            if u['errors'] == '' :
                u = u['user']
                auth_login(request,user=u)

                return redirect('profile')
            else:
                context['error'] = u['errors']

        except Exception as e : 
            context['error'] = f'Error : {e}'

    return render(request,'auth/login.html', context) 


def register (request) : 
    
    context = {}

    if request.method == "POST" : 

        try : 
            data = {
                'full_name' : request.POST.get('full_name'),
                'email' : request.POST.get('email'),
                'password' : request.POST.get('password'),
            }
            
            u = User.objects.create_user(**data)

            auth_login(request,user=u)

            return redirect('profile')
        except Exception as e : 
            context['error'] = f'Error : {e}'
        
    return render(request,'auth/register.html',context) 

