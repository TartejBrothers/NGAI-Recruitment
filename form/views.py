from django.shortcuts import render, redirect
from .forms import add_data
from django.http import Http404, HttpRequest, HttpResponse


def hello(Response):
    return HttpResponse("Hello World")


def home(request):
    form = add_data(request.POST or None)
    if form.is_valid():
        form.save()
        form = add_data()
        return redirect("https://ngairecruitment.web.app/submitted")
    dict5 = {"form": form}
    return render(request, "index.html", dict5)
