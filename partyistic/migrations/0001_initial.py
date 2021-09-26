# Generated by Django 3.2.7 on 2021-09-26 10:31

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
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Wedding', 'Wedding'), ('Graduation', 'Graduation'), ('Birthday', 'Birthday'), ('Special', 'Special')], default='Wedding', max_length=64)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Planners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('location_link', models.CharField(max_length=256)),
                ('city', models.CharField(choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Zarqa', 'Zarqa'), ('Al-Mafraq', 'Al-Mafraq'), ('Jarash', 'Jarash'), ('Ajloun', 'Ajloun'), ('As-Salt', 'As-Salt'), ('Madaba', 'Madaba'), ('karak', 'karak'), ('Tafilah', 'Tafilah'), ('Maan', 'Maan'), ('Aqaba', 'Aqaba')], default='Amman', max_length=64)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('place_type', models.CharField(choices=[('Hall', 'Hall'), ('Restaurant', 'Restaurant'), ('Farm', 'Farm')], default='Hall', max_length=64)),
                ('booked_dates', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('booked_dates', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Wedding', 'Wedding'), ('Graduation', 'Graduation'), ('Birthday', 'Birthday'), ('Special', 'Special')], default='Wedding', max_length=64)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('location_link', models.CharField(max_length=256)),
                ('city', models.CharField(choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Zarqa', 'Zarqa'), ('Al-Mafraq', 'Al-Mafraq'), ('Jarash', 'Jarash'), ('Ajloun', 'Ajloun'), ('As-Salt', 'As-Salt'), ('Madaba', 'Madaba'), ('karak', 'karak'), ('Tafilah', 'Tafilah'), ('Maan', 'Maan'), ('Aqaba', 'Aqaba')], default='Amman', max_length=64)),
                ('privacy', models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=64)),
                ('date', models.DateField()),
                ('invited_people', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MusicBands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('booked_dates', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('location_link', models.CharField(max_length=256)),
                ('city', models.CharField(choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Zarqa', 'Zarqa'), ('Al-Mafraq', 'Al-Mafraq'), ('Jarash', 'Jarash'), ('Ajloun', 'Ajloun'), ('As-Salt', 'As-Salt'), ('Madaba', 'Madaba'), ('karak', 'karak'), ('Tafilah', 'Tafilah'), ('Maan', 'Maan'), ('Aqaba', 'Aqaba')], default='Amman', max_length=64)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('location_link', models.CharField(max_length=256)),
                ('city', models.CharField(choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Zarqa', 'Zarqa'), ('Al-Mafraq', 'Al-Mafraq'), ('Jarash', 'Jarash'), ('Ajloun', 'Ajloun'), ('As-Salt', 'As-Salt'), ('Madaba', 'Madaba'), ('karak', 'karak'), ('Tafilah', 'Tafilah'), ('Maan', 'Maan'), ('Aqaba', 'Aqaba')], default='Amman', max_length=64)),
                ('price', models.IntegerField()),
                ('reviews', models.JSONField(blank=True, null=True)),
                ('booked_dates', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
