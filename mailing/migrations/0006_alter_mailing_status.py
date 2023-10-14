# Generated by Django 4.2.6 on 2023-10-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_client_owner_mailing_is_active_mailing_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('started', 'started'), ('completed', 'completed')], default='created', max_length=15, verbose_name='состояние'),
        ),
    ]