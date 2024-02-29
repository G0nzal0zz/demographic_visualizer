# Generated by Django 4.1.3 on 2024-02-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=255)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Total'), (0, 'Unknown')], default=0)),
                ('year', models.PositiveIntegerField()),
                ('inhabitants', models.PositiveBigIntegerField()),
            ],
        ),
    ]