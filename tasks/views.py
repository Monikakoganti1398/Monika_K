from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    data=Student.objects.all()
    #print(data)
    context={"data":data}
    return render(request,"index.html",context)
def create(request):
    data=Student.objects.all()
   # print(data)
    context={"data":data}
    return render(request,"create.html",context)

def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")

    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        return redirect("/")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

from django.shortcuts import render, redirect, get_object_or_404

def deleteData(request, id):
    data = get_object_or_404(Student, id=id)
    print("im hereeeeeeeeeee")
    if request.method == 'POST':

        print("im hereeeeeeeeeee insideeee")
        data.delete()
        return redirect('/')
    
        # Render the confirmation page before deleting
    return render(request, 'delete.html', {'data': data})