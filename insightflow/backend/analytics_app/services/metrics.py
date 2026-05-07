from django.db.models import Count, Sum
from django.db.models.functions import TruncDate

from analytics_app.models import Event
from analytics_app.services.retention import get_d1_retention


def apply_segment_filters(queryset, platform=None, country=None):
    if platform:
        queryset = queryset.filter(platform=platform)
    if country:
        queryset = queryset.filter(country=country)
    return queryset


def get_dau(platform=None, country=None):
    queryset = apply_segment_filters(Event.objects.all(), platform=platform, country=country)
    return (
        queryset.annotate(date=TruncDate("event_time"))
        .values("date")
        .annotate(users=Count("user_id", distinct=True))
        .order_by("date")
    )


def get_funnel(platform=None, country=None) -> dict:
    steps = ["opens_app", "signup", "start_course", "subscribe"]
    queryset = apply_segment_filters(Event.objects.all(), platform=platform, country=country)
    counts = {}
    for step in steps:
        counts[step] = queryset.filter(event_name=step).values("user_id").distinct().count()

    conversions = {}
    for index in range(1, len(steps)):
        prev_step = steps[index - 1]
        curr_step = steps[index]
        prev_count = counts[prev_step]
        conversions[f"{prev_step}_to_{curr_step}"] = (
            round((counts[curr_step] / prev_count) * 100, 2) if prev_count else 0
        )

    return {"counts": counts, "conversions_percent": conversions}


def get_revenue(platform=None, country=None) -> dict:
    queryset = apply_segment_filters(Event.objects.all(), platform=platform, country=country)
    revenue_queryset = queryset.filter(revenue__gt=0)

    total_revenue = revenue_queryset.aggregate(total=Sum("revenue"))["total"] or 0
    total_users = queryset.values("user_id").distinct().count()
    arpu = round(total_revenue / total_users, 2) if total_users else 0
    revenue_by_day = list(
        revenue_queryset.annotate(date=TruncDate("event_time"))
        .values("date")
        .annotate(revenue=Sum("revenue"))
        .order_by("date")
    )

    return {
        "total_revenue": round(total_revenue, 2),
        "arpu": arpu,
        "revenue_by_day": revenue_by_day,
    }


def get_retention():
    return get_d1_retention()
