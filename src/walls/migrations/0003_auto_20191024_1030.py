# Generated by Django 2.2.6 on 2019-10-24 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('walls', '0002_auto_20191022_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wall',
            name='owner',
        ),
        migrations.AlterField(
            model_name='card',
            name='int_indicator',
            field=models.SmallIntegerField(choices=[(-1, '- Off -'), (0, '0'), (1, '1'), (2, '2'), (3, '3')], default=-1),
        ),
        migrations.CreateModel(
            name='WallMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(max_length=80, verbose_name='Roles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walls.Wall')),
            ],
        ),
        migrations.AddField(
            model_name='wall',
            name='membership',
            field=models.ManyToManyField(through='walls.WallMembership', to=settings.AUTH_USER_MODEL),
        ),
    ]