from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    now = datetime.now()
    ny = False
    if now.day == 1 and now.month == 1:
        ny = True
    return render (request, "newyear/index.html", {
        "newyear": ny
    })
