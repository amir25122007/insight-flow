import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics_app.services.metrics import get_dau, get_funnel, get_retention, get_revenue


class DAUView(APIView):
    def get(self, request):
        platform = request.query_params.get("platform")
        country = request.query_params.get("country")
        data = list(get_dau(platform=platform, country=country))
        return Response(data)


class FunnelView(APIView):
    def get(self, request):
        platform = request.query_params.get("platform")
        country = request.query_params.get("country")
        data = get_funnel(platform=platform, country=country)
        return Response(data)


class RetentionView(APIView):
    def get(self, request):
        data = get_retention()
        return Response(data)


class RevenueView(APIView):
    def get(self, request):
        platform = request.query_params.get("platform")
        country = request.query_params.get("country")
        data = get_revenue(platform=platform, country=country)
        return Response(data)


def dashboard_view(request):
    dau_data = list(get_dau())
    context = {
        "dau": dau_data,
        "funnel": get_funnel(),
        "retention": get_retention(),
        "revenue": get_revenue(),
        "dau_labels": json.dumps([str(item["date"]) for item in dau_data]),
        "dau_values": json.dumps([item["users"] for item in dau_data]),
    }
    return render(request, "dashboard.html", context)
