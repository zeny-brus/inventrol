# Generated by Django 4.2.1 on 2023-05-28 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_movement_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product'),
        ),
    ]
