# Generated by Django 4.2.1 on 2023-06-02 08:18

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.CharField(choices=[('танк', 'танк'), ('хил', 'хил'), ('дд', 'дд'), ('торговец', 'торговец'), ('гильдмастер', 'гильдмастер'), ('квестгивер', 'квестгивер'), ('кузнец', 'кузнец'), ('кожевник', 'кожевник'), ('зельевар', 'зельевар'), ('мастер заклинаний', 'мастер заклинаней')], default='торговец', max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Reply')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('accept', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
