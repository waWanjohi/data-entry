# Generated by Django 4.2.3 on 2023-07-03 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_created=True, auto_now=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_created=True, auto_now=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("attachment", models.URLField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "NEW"),
                            ("UNDER_REVIEW", "UNDER_REVIEW"),
                            ("PUBLISHED", "PUBLISHED"),
                        ],
                        default="NEW",
                        max_length=50,
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assigned_entries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_entry.category",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("category", "name")},
            },
        ),
        migrations.CreateModel(
            name="EventEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_created=True, auto_now=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("event_name", models.CharField(max_length=30, unique=True)),
                ("location", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("event_date", models.DateTimeField()),
                (
                    "event_organizer_email",
                    models.EmailField(max_length=254, unique=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HealthInstitutionEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_created=True, auto_now=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("phone_number", models.CharField(max_length=50, unique=True)),
                ("country", models.CharField(max_length=50, unique=True)),
                (
                    "official_email_address",
                    models.EmailField(max_length=254, unique=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProfessionEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_created=True, auto_now=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField()),
                ("occupation", models.CharField(max_length=50, unique=True)),
                ("minimum_entry_age", models.PositiveIntegerField(unique=True)),
                ("is_gender_agnostic", models.BooleanField(default=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProfessionEntryChangeLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("action", models.CharField(max_length=150)),
                (
                    "entry_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_entry.professionentry",
                    ),
                ),
                (
                    "event_triggered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HealthInstitutionEntryChangeLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("action", models.CharField(max_length=150)),
                (
                    "entry_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_entry.healthinstitutionentry",
                    ),
                ),
                (
                    "event_triggered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventEntryChangeLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("action", models.CharField(max_length=150)),
                (
                    "entry_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_entry.evententry",
                    ),
                ),
                (
                    "event_triggered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomEntryChangeLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_created=True, auto_now_add=True),
                ),
                ("action", models.CharField(max_length=150)),
                (
                    "entry_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_entry.customentry",
                    ),
                ),
                (
                    "event_triggered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
