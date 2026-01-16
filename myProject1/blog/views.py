from django.http import HttpResponse
def Home(request):
   return HttpResponse("Welcome To The Blog Home Page")

def About(request):
   return HttpResponse("About Page of the Blog")