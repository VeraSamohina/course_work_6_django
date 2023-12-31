# Generated by Django 4.2.5 on 2023-09-24 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='комментарии')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('body', models.TextField(verbose_name='текст рассылки')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='начало рассылки')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='конец рассылки')),
                ('title', models.CharField(max_length=150, verbose_name='название рассылки')),
                ('period', models.CharField(choices=[('one', 'один раз'), ('daily', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'ежемесячно')], default='one', max_length=9)),
                ('status', models.CharField(choices=[('new', 'создана'), ('active', 'запущена'), ('end', 'завершена')], default='new', max_length=9)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('clients', models.ManyToManyField(to='mailing.client', verbose_name='клиенты')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.message', verbose_name='текст рассылки')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='время')),
                ('status', models.CharField(max_length=20, verbose_name='статус')),
                ('response', models.TextField(blank=True, verbose_name='ответ сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='рассылка')),
            ],
        ),
    ]
