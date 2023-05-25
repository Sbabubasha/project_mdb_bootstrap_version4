from django.shortcuts import render

# Create your views here.
def mdb_bootstrap(request):
    return render(request,'mdbv4.html')