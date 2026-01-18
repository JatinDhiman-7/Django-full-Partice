from django.shortcuts import render
from django.contrib import messages

def show_message(request):
    messages.debug(request,'This is a debug message.')
    messages.info(request,'This is an info message. ')
    return render(request,'message.html')


