from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        "author": "Disha",
        "content": "Life",
        "title": "Life as we know it",
        "Posted_Date": "Today",
    },
    {
        "author": "Diya",
        "content": "Dance",
        "title": "ABCD",
        "Posted_Date": "Yesterday",
    },
]
# Create your views here.
def home_page(request):
    context = {"posts": posts}
    return render(request, "blogy.html", context)
def blog(request):
    return HttpResponse("Blog Home")