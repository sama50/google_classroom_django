# Generated by Django 4.1.3 on 2023-03-06 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_joinbyclassroom_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='date',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
