import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .models import Fundings, History


# Create your views here.
def mainpage(request):
    popular_presents = Fundings.objects.filter(type="PRESENT").order_by("-likes_cnt")[
        :2
    ]
    popular_sosos = Fundings.objects.filter(type="SOSO").order_by("-likes_cnt")[:2]
    return render(
        request,
        "main/mainpage.html",
        {
            "popular_presents": popular_presents,
            "popular_sosos": popular_sosos,
        },
    )


def payhistory(request):
    if request.user.is_authenticated:
        pay_lists = History.objects.filter(user=request.user)
        return render(request, "main/payhistory.html", {"pay_lists": pay_lists})
    else:
        return redirect("accounts:login")


def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            new_fundings = Fundings()
            new_fundings.type = request.POST["type"]
            new_fundings.title = request.POST["title"]
            new_fundings.writer = request.user
            new_fundings.product = request.POST["product"]
            new_fundings.total_price = request.POST["total_price"]
            new_fundings.content = request.POST["content"]
            new_fundings.start_date = timezone.now()
            new_fundings.end_date = request.POST["end_date"]
            new_fundings.funding_image = request.FILES.get("funding_image")
            new_fundings.is_private = request.POST.get("is_private", False)
            new_fundings.qr_image = request.FILES.get("qr_image")
            new_fundings.save()
            return redirect("main:detail", new_fundings.id)


def choose(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_type = request.POST["type"]
            return render(request, "main/create.html", {"selected_type": selected_type})
        elif request.method == "GET":
            return render(request, "main/choose.html")
    else:
        return redirect("accounts:login")


def detail(request, funding_id):
    funding = get_object_or_404(Fundings, pk=funding_id)
    encoded_funding_id = base64.b64encode(str(funding.id).encode()).decode()
    delievery_date = funding.end_date + timedelta(days=2)
    request.session["encoded_funding_id"] = encoded_funding_id
    return render(
        request,
        "main/detail.html",
        {
            "funding": funding,
            "delievery_date": delievery_date,
        },
    )


def update(request, funding_id):
    funding = get_object_or_404(Fundings, pk=funding_id)
    if request.user == funding.writer:
        if request.method == "POST":
            funding.title = request.POST["title"]
            funding.content = request.POST["content"]
            funding.funding_image = request.FILES.get("funding_image")
            funding.qr_image = request.FILES.get("qr_image")
            funding.save()
            return redirect("main:detail", funding.id)
        elif request.method == "GET":
            return render(request, "main/edit.html", {"funding": funding})
    else:
        return redirect("main:detail", funding.id)


def present(request):
    present_fundings = Fundings.objects.filter(type="PRESENT")
    return render(
        request,
        "main/present.html",
        {
            "present_fundings": present_fundings,
        },
    )


def soso(request):
    soso_fundings = Fundings.objects.filter(type="SOSO")
    return render(
        request,
        "main/soso.html",
        {
            "soso_fundings": soso_fundings,
        },
    )


def dream(request):
    dream_fundings = Fundings.objects.filter(type="DREAM")
    return render(
        request,
        "main/dream.html",
        {
            "dream_fundings": dream_fundings,
        },
    )


def delete(request, funding_id):
    funding = get_object_or_404(Fundings, pk=funding_id)
    if request.user == funding.writer:
        funding.delete()
        return redirect("main:mainpage")
    else:
        return redirect("main:detail", funding.id)


def like(request, funding_id):
    if request.user.is_authenticated:
        funding = get_object_or_404(Fundings, pk=funding_id)
        if request.user in funding.like.all():
            funding.like.remove(request.user)
            funding.likes_cnt -= 1
            funding.save()
        else:
            funding.like.add(request.user)
            funding.likes_cnt += 1
            funding.save()
        return redirect("main:detail", funding.id)
    else:
        return redirect("accounts:login")
