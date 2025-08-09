from django.shortcuts import render
import random

# Create your views here.
def index(request):
    random_num=  random.randint(0,100)
    return render(request,"home.html",context={"ran":random_num})