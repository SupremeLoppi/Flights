# Generated by Django 4.2 on 2023-05-09 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FlightCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
                ('popularity', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('most popular', 'most popular'), ('least popular', 'least popular')], max_length=69)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_namep', to='home.city')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('pricing', models.IntegerField(choices=[(500, '500'), (1000, '1000'), (800, '800'), (300, '300'), (200, '200')])),
                ('duration', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('standard', models.CharField(choices=[('high class', 'high class'), ('middle class', 'middle class'), ('business class', 'business class')], max_length=50)),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departurex', to='home.airport')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinationx', to='home.airport')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_company', to='home.flightcompany')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='Country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countryx', to='home.country'),
        ),
        migrations.AddField(
            model_name='airport',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_name', to='home.city'),
        ),
    ]
