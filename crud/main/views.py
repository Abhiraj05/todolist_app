from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        taskname=request.POST.get("taskname")
        return HttpResponse(f"task:{taskname}")
    return render(request,"home.html")