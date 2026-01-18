from django.shortcuts import render
from .forms import StudentForm
from .models import Student
def student_create(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render(request,'student_form.html',{'form':form})
    

def Student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})
