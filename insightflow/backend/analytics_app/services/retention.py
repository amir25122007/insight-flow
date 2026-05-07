from datetime import timedelta

from django.db.models.functions import TruncDate

from analytics_app.models import Event


def get_d1_retention() -> list[dict]:
    first_seen_rows = (
        Event.objects.annotate(event_date=TruncDate("event_time"))
        .values("user_id", "event_date")
        .order_by("user_id", "event_date")
    )

    first_seen_by_user = {}
    activity_by_day = {}
    for row in first_seen_rows:
        user_id = row["user_id"]
        event_date = row["event_date"]
        first_seen_by_user.setdefault(user_id, event_date)
        activity_by_day.setdefault(event_date, set()).add(user_id)

    retention = []
    for cohort_day in sorted(activity_by_day.keys()):
        cohort_users = {uid for uid, day in first_seen_by_user.items() if day == cohort_day}
        if not cohort_users:
            continue

        next_day_users = activity_by_day.get(cohort_day + timedelta(days=1), set())
        returned_users = cohort_users.intersection(next_day_users)
        retention_rate = len(returned_users) / len(cohort_users) if cohort_users else 0
        retention.append(
            {
                "cohort_day": cohort_day,
                "cohort_size": len(cohort_users),
                "returned_users": len(returned_users),
                "d1_retention": round(retention_rate, 4),
            }
        )

    return retention
