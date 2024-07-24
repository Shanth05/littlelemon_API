# Generated by Django 4.1.6 on 2023-02-06 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('littlelemon', '0017_alter_order_delivery_crew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='delivered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cartitem',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderitem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='littlelemon.orderitem')),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='purchase',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='littlelemon.purchases'),
        ),
    ]