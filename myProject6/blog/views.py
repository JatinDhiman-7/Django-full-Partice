from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_details(request):
    post={
        "title":"My second Templates Post",
        "description":"Django is web framework and most use in web application",
        "author":None,
        "created_at":datetime(2025,8,19,10,30),
        "comments_count":5,
        "tags":["Django","Python","web Development"],
        "price":100,
        "number":7,
    }
    return render(request,'blog/blog_details.html',{"post":post})
