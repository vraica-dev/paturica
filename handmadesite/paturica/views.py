from django.contrib import messages
from django.shortcuts import render, redirect
from paturica.models import HandMadePic, Produs
from paturica.forms import ContactMessageForm


def home(request):
    all_carousel = HandMadePic.objects.filter(in_carousel=True)
    return render(request, "index.html", {"pics": all_carousel})


def register_message(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message succefully sent. Thank you!")
        return redirect("home-page")
    else:
        form = ContactMessageForm()
    return render(request, "index.html", {"form": form})


def detail(request, pic_id):
    obj = Produs.objects.get(pic=pic_id)
    return render(request, 'detail.html', {'produs':obj})
