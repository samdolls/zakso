from django.shortcuts import render, get_object_or_404, redirect
from main.models import Fundings, History

import os, requests, json, base64, time


def index(request):
    if request.user.is_authenticated:
        user_info = {
            "name": request.user.username,
            "customer_key": request.user.customer_key,
        }
    else:
        return redirect("accounts:login_view")
    encoded_funding_id = request.session.get("encoded_funding_id")
    funding_id = base64.b64decode(encoded_funding_id).decode()
    funding = get_object_or_404(Fundings, pk=funding_id)
    return render(
        request,
        "payments/index.html",
        {
            "user_info": user_info,
            "funding": funding,
        },
    )


def success(request):
    orderId = request.GET.get("orderId")
    amount = request.GET.get("amount")
    paymentKey = request.GET.get("paymentKey")
    encoded_funding_id = request.session.get("encoded_funding_id")
    funding_id = base64.b64decode(encoded_funding_id).decode()
    funding = get_object_or_404(Fundings, pk=funding_id)
    if funding.total_price < funding.accumulation + int(amount):
        return render(
            request,
            "payments/fail.html",
            {
                "code": "403",
                "message": "펀딩 금액을 초과하여 결제할 수 없습니다.",
            },
        )

    url = "https://api.tosspayments.com/v1/payments/confirm"

    """
    개발자센터에 로그인해서 내 결제위젯 시크릿 키를 입력하세요. 시크릿 키는 외부에 공개되면 안돼요.
    @docs https://docs.tosspayments.com/reference/using-api/api-keys
  """
    secretKey = os.getenv("TOSS_SECRET_KEY")

    """
    토스페이먼츠 API는 시크릿 키를 사용자 ID로 사용하고, 비밀번호는 사용하지 않습니다.
    비밀번호가 없다는 것을 알리기 위해 시크릿 키 뒤에 콜론을 추가합니다.
    @docs https://docs.tosspayments.com/reference/using-api/authorization#basic-인증-방식이란
  """
    userpass = secretKey + ":"
    encoded_u = base64.b64encode(userpass.encode()).decode()

    headers = {
        "Authorization": "Basic %s" % encoded_u,
        "Content-Type": "application/json",
    }

    params = {
        "orderId": orderId,
        "amount": amount,
        "paymentKey": paymentKey,
    }

    res = requests.post(url, data=json.dumps(params), headers=headers)
    resjson = res.json()

    respaymentKey = resjson["paymentKey"]
    resorderId = resjson["orderId"]
    accumulation = resjson["totalAmount"]

    try:
        current_accumulation = funding.accumulation
        funding.accumulation = current_accumulation + int(amount)
        funding.save()
        History.objects.create(user=request.user, funding=funding, amount=amount)
        order_number = History.objects.filter(funding=funding).count()
    except Fundings.DoesNotExist:
        return render(
            request,
            "payments/fail.html",
            {"code": "404", "message": "존재하지 않는 펀딩입니다."},
        )

    return render(
        request,
        "payments/success.html",
        {
            "respaymentKey": respaymentKey,
            "resorderId": resorderId,
            "accumulation": accumulation,
            "funding": funding,
            "order_number": order_number,
        },
    )


def fail(request):
    code = request.GET.get("code")
    message = request.GET.get("message")

    return render(
        request,
        "payments/fail.html",
        {
            "code": code,
            "message": message,
        },
    )
