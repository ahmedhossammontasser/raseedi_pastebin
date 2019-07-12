# Generated by Django 2.2.3 on 2019-07-11 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pastebin', '0002_paste_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typepaste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='paste',
            name='name',
        ),
        migrations.AddField(
            model_name='paste',
            name='allowedusers',
            field=models.ManyToManyField(related_name='allowedusers', to=settings.AUTH_USER_MODEL, verbose_name='list of allowed users'),
        ),
        migrations.AlterField(
            model_name='paste',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paste',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pastebin.Typepaste'),
        ),
    ]
