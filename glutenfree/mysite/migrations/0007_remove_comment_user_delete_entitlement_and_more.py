# Generated by Django 5.0.7 on 2024-08-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_commentrecipe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Entitlement',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]