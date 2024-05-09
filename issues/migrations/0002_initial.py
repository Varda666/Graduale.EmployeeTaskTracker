# Generated by Django 4.2.8 on 2024-05-09 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='email', verbose_name='владелец проекта'),
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_executor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='executed_issues', to=settings.AUTH_USER_MODEL, to_field='email', verbose_name='исполнитель'),
        ),
        migrations.AddField(
            model_name='issue',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_issues', to=settings.AUTH_USER_MODEL, to_field='email', verbose_name='постановщик задачи'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='issues.project', verbose_name='название проекта'),
        ),
    ]
