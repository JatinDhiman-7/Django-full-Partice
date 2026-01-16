from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_list(request):
    blogs=[
        {
           "title":"Django Basics",
           "is_featured":True,
           "author":"Mohit Kumar",
        },
        {
           "title":"Django Advanced",
           "is_featured":False,
           "author":" ",
        },
        {
           "title":"Django Rest Framework",
           "is_featured":True,
           "author":"Anu Chouduary",
        }
    ]
    context={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1>Welcome to My Blog</h1>"
    }
    return render(request,'blog/blog_list.html',context)