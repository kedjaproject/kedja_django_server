# Generated by Django 2.2.6 on 2019-10-22 14:07

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
            name='Wall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('wall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walls.Wall')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('int_indicator', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walls.Collection')),
                ('relations', models.ManyToManyField(blank=True, related_name='_card_relations_+', to='walls.Card', verbose_name='Relations')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
