from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_id", models.IntegerField()),
                ("event_name", models.CharField(max_length=100)),
                ("event_time", models.DateTimeField()),
                ("platform", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=50)),
                ("session_id", models.CharField(max_length=100)),
                ("revenue", models.FloatField(default=0)),
            ],
        ),
        migrations.AddIndex(
            model_name="event",
            index=models.Index(fields=["user_id"], name="analytics_ap_user_id_05f31f_idx"),
        ),
        migrations.AddIndex(
            model_name="event",
            index=models.Index(fields=["event_name"], name="analytics_ap_event_n_96792f_idx"),
        ),
        migrations.AddIndex(
            model_name="event",
            index=models.Index(fields=["event_time"], name="analytics_ap_event_t_82ce47_idx"),
        ),
    ]
