from pathlib import Path

import pandas as pd
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime

from analytics_app.models import Event


class Command(BaseCommand):
    help = "Load events from CSV into Event table."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            default=str(Path(__file__).resolve().parents[5] / "data" / "sample_events.csv"),
            help="Path to CSV file with events.",
        )

    def handle(self, *args, **options):
        csv_path = options["path"]
        df = pd.read_csv(csv_path)

        events = []
        for _, row in df.iterrows():
            events.append(
                Event(
                    user_id=int(row["user_id"]),
                    event_name=row["event_name"],
                    event_time=parse_datetime(str(row["event_time"])),
                    platform=row["platform"],
                    country=row["country"],
                    session_id=row["session_id"],
                    revenue=float(row["revenue"]),
                )
            )

        Event.objects.bulk_create(events, batch_size=1000)
        self.stdout.write(self.style.SUCCESS(f"Loaded {len(events)} events from {csv_path}"))
