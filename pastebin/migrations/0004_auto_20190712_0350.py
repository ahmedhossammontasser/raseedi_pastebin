# Generated by Django 2.2.3 on 2019-07-12 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0003_auto_20190711_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='allowedusers',
            field=models.ManyToManyField(blank=True, null=True, related_name='allowedusers', to=settings.AUTH_USER_MODEL, verbose_name='list of allowed users'),
        ),
        migrations.AlterField(
            model_name='paste',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pastes', to='pastebin.Typepaste'),
        ),
    ]
