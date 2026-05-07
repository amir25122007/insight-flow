from django.db import models


class Event(models.Model):
    user_id = models.IntegerField()
    event_name = models.CharField(max_length=100)
    event_time = models.DateTimeField()
    platform = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    session_id = models.CharField(max_length=100)
    revenue = models.FloatField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["user_id"]),
            models.Index(fields=["event_name"]),
            models.Index(fields=["event_time"]),
        ]

    def __str__(self) -> str:
        return f"{self.user_id} {self.event_name} {self.event_time}"
