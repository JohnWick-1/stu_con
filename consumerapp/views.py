from django.shortcuts import render
from .models import StudentCon
from .serializers import StudentConSerializer
from rest_framework.viewsets import ModelViewSet
import requests
import datetime
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
import json

PRO_URL='http://127.0.0.1:8002/pro/student/'
CH_URL = 'http://127.0.0.1:8002/check/'

class StudentConViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StudentConSerializer
    queryset = StudentCon.objects.all()




def home(request):
    date = datetime.datetime.now()
    list_of_student = StudentCon.objects.all()
    last_obj=StudentCon.objects.last().__dict__.get('first_name')
    all_data={'date':date,'last_obj':last_obj,'list':list_of_student}

    return render(request,'capp/student_form.html',context=all_data)


from django.middleware import csrf
# @csrf_exempt    #cross site request forgery/one click attack /session ridding
def student_save(request):
    date = datetime.datetime.now()
    list_of_student = StudentCon.objects.all()
    csrf_tok=csrf.get_token(request)
    print("CSRF token : ",csrf_tok)
    idt=request.POST['id']

    try:
        id= int(request.POST['id'])

    except:

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        phone_no = request.POST['phone_nu']
        dob = request.POST['dob']
        country = request.POST['country']

        obj = StudentCon(first_name=first_name, last_name=last_name, phone_nu=phone_no, dob=dob, country=country,
                      status=True,)
        # status add here
        obj.save()
        data={"first_name": first_name,"last_name": last_name}

        response=requests.post(PRO_URL,data=data)
        print(response)
        password=response.json()
        print(type(password))
        print(password.get('password'))
        obj.password=password.get('password')
        obj.save()

        # print(response.text)

        print(response.status_code)

        last_obj = StudentCon.objects.last().__dict__.get('first_name')
        all_data = {'date': date, 'last_obj': last_obj, 'list': list_of_student, }
        return render(request, 'capp/student_form.html', context=all_data)

    else:

        StudentCon.objects.filter(id=idt).update(first_name=request.POST['firstname'],
                                         last_name=request.POST['lastname'],
                                         phone_nu=request.POST["phone_nu"],
                                         dob=request.POST['dob'],
                                         country=request.POST['country'],
                                         )
        last_obj = StudentCon.objects.last().__dict__.get('first_name')
        all_data = {'date': date, 'last_obj': last_obj, 'list': list_of_student, }
        return render(request, 'capp/student_form.html', context=all_data)



def update(request,id):
    date = datetime.datetime.now()
    list_of_student = StudentCon.objects.all()
    last_obj=StudentCon.objects.last().__dict__.get('first_name')
    entry = StudentCon.objects.get(id=id)


    all_data = {'date': date, 'last_obj': last_obj, 'list': list_of_student, 'entry':entry}
    return render(request, 'capp/student_form.html', context=all_data)


def delete(request,id):
    date = datetime.datetime.now()
    list_of_student = StudentCon.objects.all()
    last_obj=StudentCon.objects.last().__dict__.get('first_name')

    StudentCon.objects.filter(id=id).update(status=False)
    all_data={'date':date,'last_obj':last_obj,'list':list_of_student,}

    return render(request,'capp/student_form.html',context=all_data)


def on(request,id):
    date = datetime.datetime.now()
    list_of_student = StudentCon.objects.all()
    last_obj=StudentCon.objects.last().__dict__.get('first_name')
    StudentCon.objects.filter(id=id).update(status=True)
    all_data={'date':date,'last_obj':last_obj,'list':list_of_student,}

    return render(request,'capp/student_form.html',context=all_data)




def test1(response):
    response = requests.get(PRO_URL)
    print(response)
    l = response.json()
    print(type(l))
    print(l)
    from django.http import HttpResponse
    return HttpResponse('<html><body>inside get <br>{%for i in l%} <br>{{i}}<br>{%endfor%}</body></html',{'l':l})


def test2(response,id):
    response = requests.get(url='http://127.0.0.1:8002/pro/student/'+str(id)+'/')
    print(response)
    password = response.json()
    print(type(password))
    print(password.get('password'))
    from django.http import HttpResponse
    return HttpResponse('<h1>inside get</h1>')

def test3(response,id):
    response = requests.delete(url='http://127.0.0.1:8002/pro/student/'+str(id)+'/')
    print(response)
    data=response.json()
    print(type(data))
    print(data)

    from django.http import HttpResponse
    return HttpResponse('<h1>inside delete</h1>')
