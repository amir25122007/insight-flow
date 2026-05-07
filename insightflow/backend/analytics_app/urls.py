from django.urls import path

from .views import DAUView, FunnelView, RetentionView, RevenueView, dashboard_view


urlpatterns = [
    path("metrics/dau/", DAUView.as_view(), name="metrics-dau"),
    path("metrics/funnel/", FunnelView.as_view(), name="metrics-funnel"),
    path("metrics/retention/", RetentionView.as_view(), name="metrics-retention"),
    path("metrics/revenue/", RevenueView.as_view(), name="metrics-revenue"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
