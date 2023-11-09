import base64
import json
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import timedelta, date, datetime
from django.http import HttpResponse, JsonResponse
from django.db.models import F

from .models import Fundings, History


# Create your views here.
def mainpage(request):
    popular_presents = Fundings.objects.filter(
        type="선물 펀딩", accumulation__lt=F("total_price")
    ).order_by("-likes_cnt")[:3]
    popular_sosos = Fundings.objects.filter(type="소소 펀딩").order_by("-likes_cnt")[:3]
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


def before_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            type = request.POST["type"]
            title = request.POST["fundName"]
            product = request.POST["productName"]
            total_price = request.POST["setPrice"]
            content = request.POST["fundStory"]
            year = int(request.POST["setYear"])
            month = int(request.POST["setMonth"])
            day = int(request.POST["setDay"])
            funding_image = request.FILES.get("img")
            print(funding_image)
            if funding_image:
                fs = FileSystemStorage(location="media/fundings/")
                filename = fs.save(funding_image.name, funding_image)
                funding_image_path = fs.url(filename)
            is_private = request.POST.get("is_private", False)
            request.session["post_info"] = {
                "type": type,
                "title": title,
                "product": product,
                "total_price": total_price,
                "content": content,
                "setYear": year,
                "setMonth": month,
                "setDay": day,
                "funding_image": funding_image_path,
                "is_private": is_private,
            }
            return redirect("main:create")
    return render(request, "main/before_create.html")


def create(request):
    post_info = request.session.get("post_info", None)
    print(post_info["funding_image"])
    if request.user.is_authenticated:
        if request.method == "POST":
            new_fundings = Fundings()
            new_fundings.type = post_info["type"]
            new_fundings.title = post_info["title"]
            new_fundings.writer = request.user
            new_fundings.product = post_info["product"]
            new_fundings.total_price = post_info["total_price"]
            new_fundings.content = post_info["content"]
            new_fundings.start_date = timezone.now()
            year = int(post_info["setYear"])
            month = int(post_info["setMonth"])
            day = int(post_info["setDay"])
            end_date = date(year, month, day)
            new_fundings.end_date = end_date
            funding_image_path = post_info["funding_image"].replace(
                settings.MEDIA_URL, "fundings/"
            )
            new_fundings.funding_image = funding_image_path
            new_fundings.is_private = post_info.get("is_private", False)
            new_fundings.account_num = request.POST["account_num"]
            new_fundings.delievery = request.POST["delievery"]
            # new_fundings.qr_image = request.FILES.get("qr_image")
            new_fundings.save()
            return redirect("main:detail", new_fundings.id)
        elif request.method == "GET":
            return render(request, "main/create.html")


def choose(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            selected_type = request.POST["type"]
            return render(
                request, "main/before_create.html", {"selected_type": selected_type}
            )
        elif request.method == "GET":
            return render(request, "main/choose.html")
    else:
        return redirect("accounts:login_view")


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
    present_fundings = Fundings.objects.filter(
        type="선물 펀딩", accumulation__lt=F("total_price")
    ).order_by("-created_at")
    count = present_fundings.count()
    return render(
        request,
        "main/present.html",
        {
            "present_fundings": present_fundings,
            "count": count,
        },
    )


def soso(request):
    soso_fundings = Fundings.objects.filter(
        type="소소 펀딩", accumulation__lt=F("total_price")
    ).order_by("-created_at")
    count = soso_fundings.count()
    return render(
        request,
        "main/soso.html",
        {
            "soso_fundings": soso_fundings,
            "count": count,
        },
    )


def dream(request):
    dream_fundings = Fundings.objects.filter(type="드림 펀딩")
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


def funding_like_toggle(request):
    if request.user.is_authenticated:  # 유저가 로그인했으면
        pk = request.GET["pk"]
        funding = get_object_or_404(
            Fundings, pk=pk
        )  # URL 매핑으로 받은 게시물 아이디에 해당하는 게시물을 담음
        if (
            request.user in funding.like.all()
        ):  # 게시물의 like 안에 있는 모든 유저들 중에 현재 유저가 있는지 판별
            funding.like.remove(
                request.user
            )  # 이미 좋아요가 눌러진 상태라는 것이기에 좋아요를 누르면 like안에 있는 유저들 중 자기를 없앰
            funding.likes_cnt -= 1  # 좋아요 개수 1개 줄음
            funding.save()  # 저장
            result = "like_cancel"
        else:
            funding.like.add(request.user)  # 좋아요를 누르면 like 안에 유저 추가
            funding.likes_cnt += 1  # 좋아요 1개 추가
            funding.save()
            result = "like"

        context = {"likes_cnt": funding.likes_cnt, "result": result}

        return HttpResponse(json.dumps(context), content_type="application/json")
    # else:
    #     return render(request, "accounts/no_auth.html")
