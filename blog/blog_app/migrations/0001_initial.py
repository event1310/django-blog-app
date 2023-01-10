# Generated by Django 4.1.5 on 2023-01-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]