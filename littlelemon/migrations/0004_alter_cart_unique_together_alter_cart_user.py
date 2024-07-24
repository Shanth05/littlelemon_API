# Generated by Django 4.1.6 on 2023-02-04 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('littlelemon', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
