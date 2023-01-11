# Generated by Django 4.0.7 on 2022-12-05 12:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ads", "0002_ad_content_type_ad_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                    "text",
                    models.TextField(
                        validators=[
                            django.core.validators.MinLengthValidator(
                                3, "Comment must be greater than 3 characters"
                            )
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="ad",
            name="comments",
            field=models.ManyToManyField(
                related_name="comments_owned",
                through="ads.Comment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="ad",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ads.ad"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
