from django.http import HttpResponse
def Home(request):
   return HttpResponse("Welcome To The Shop Home Page")

def products(request):
   return HttpResponse("Shop Product Page")