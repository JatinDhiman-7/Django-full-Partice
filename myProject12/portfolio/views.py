from django.shortcuts import render


def student_list(request):
    return render(request,'portfolio/student_list.html')