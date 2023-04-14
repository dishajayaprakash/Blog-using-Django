from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        "author": "Disha",
        "auth_url": "https://www.imdb.com/title/tt1055292/"
        "content" : "Life",
        "title": "Life as we know it",
        "Posted_Date": "Today",
    },
    {
        "author": "Diya",
        "auth_url": "https://www.imdb.com/title/tt2321163/"
        "content" : "Dance",
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
