# Generated by Django 3.1.2 on 2020-11-03 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bag",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="RSAKey",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key_name", models.CharField(max_length=50)),
                ("comment", models.TextField(blank=True, null=True)),
                ("public_key", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Sample",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("barcode", models.CharField(max_length=50)),
                ("access_code", models.CharField(max_length=50)),
                ("rack", models.CharField(blank=True, max_length=50, null=True)),
                ("password_hash", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "bag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, related_name="samples", to="app.bag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("name_encrypted", models.CharField(max_length=200)),
                ("address_encrypted", models.CharField(max_length=200)),
                ("contact_encrypted", models.CharField(max_length=200)),
                ("public_key_fingerprint", models.CharField(max_length=200)),
                ("session_key_encrypted", models.CharField(max_length=1000)),
                ("aes_instance_iv", models.CharField(max_length=200)),
                (
                    "sample",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="registrations", to="app.sample"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(max_length=50)),
                ("comment", models.TextField(blank=True, null=True)),
                ("updated_on", models.DateTimeField(auto_now_add=True)),
                (
                    "sample",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="events", to="app.sample"
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bag",
            name="rsa_key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, related_name="bags", to="app.rsakey"
            ),
        ),
    ]
