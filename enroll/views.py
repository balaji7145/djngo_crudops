from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrtion
from .models import User
# Create your views here.
#this function will add new item n show all item
def add_show(request):
    if request.method=="POST":
        fm=StudentRegistrtion(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pm=fm.cleaned_data['password']
            reg= User(name=nm,email=em,password=pm)
            fm.save()
            fm=StudentRegistrtion()
    else:
        fm=StudentRegistrtion()
    stud=User.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm, 'stud':stud})

#this function is for editing
def update_data(request, id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistrtion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistrtion(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})


#this function will delete
def delete_data(request, id):
    if request.method == "POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')





   
