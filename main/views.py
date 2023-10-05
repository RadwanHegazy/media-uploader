from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from uuid import uuid4
from .models import File
import ast, threading, os, time


@login_required
def profile (request) :

    context = {
        'files' : File.objects.filter(user=request.user).order_by('-date').values('name','uuid')
    }



    if 'file' in request.FILES :

        file = request.FILES['file']
        data = file.readlines()
        
        f = File.objects.create(
            user = request.user,
            name = file.name,
            file_data = data,
            uuid = uuid4()
        )

        return redirect('profile')

    if 'delete' in request.GET : 
        file_uuid = request.GET['delete']
        File.objects.get(uuid=file_uuid).delete()
        return redirect('profile')
 
    return render(request,'main/profile.html',context)



def del_fnuc (name) :
    
    while True : 
        try :
            os.remove(name)
            break
        except Exception  :
            pass


@login_required
def download (request, fileuuid) :

    file = get_object_or_404(File,uuid=fileuuid)
    data = ast.literal_eval(file.file_data)

    path = "media\\"+file.name
    with open (path,'wb') as f :
        f.writelines(data)

    
        
    t = threading.Thread(target=del_fnuc,args=(path,))
    t.start()

    return FileResponse(open(path,'rb'))

