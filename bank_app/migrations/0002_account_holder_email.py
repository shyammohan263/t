# Generated by Django 4.0.2 on 2022-02-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='holder_email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
