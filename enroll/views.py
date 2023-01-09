from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.decorators.http import require_http_methods


# Create your views here.
def addand_show(request):
    if request.method == 'POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg= User(name=nm, email=em, password=pw)
            reg.save()
            response = render(request,'enroll/row.html',{'form':fm,'st':reg})
            response['HX-Trigger']='formReset'
            return response
    else:
        fm=StudentRegistration()
    
    stud=User.objects.all()
        
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})

    
# def delete(request,id):
#     if request.method=='POST':
#         de=User.objects.get(pk=id)
#         de.delete()
#     return HttpResponseRedirect('/')


@require_http_methods(['POST'])
def deleteall(request):
    dea=User.objects.all()
    dea.delete()
    return render(request,'enroll/table.html',{'stu':[]})



@require_http_methods(['POST'])
def delete(request,id):
    de=User.objects.filter(pk=id)
    de.delete()
    return JsonResponse({'detail':'Deleted'},safe=False)

def updatedata(request,id):
    return render(request, 'enroll/update.html', {'id':id})




@require_http_methods(['POST'])
def deleteselected(request):
    des=User.objects.filter(id__in=request.POST.getlist('delete'))
    des.delete()
    return render(request,'enroll/table.html',{'stu':User.objects.all()})






