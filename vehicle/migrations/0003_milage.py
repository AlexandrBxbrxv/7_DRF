# Generated by Django 4.2.2 on 2024-10-23 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milage', models.PositiveIntegerField(verbose_name='пробег')),
                ('year', models.SmallIntegerField(verbose_name='год регистрации')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage_car', to='vehicle.car', verbose_name='машина')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage_moto', to='vehicle.moto', verbose_name='мотоцикл')),
            ],
            options={
                'verbose_name': 'пробег',
                'verbose_name_plural': 'пробег',
                'ordering': ('-year',),
            },
        ),
    ]
