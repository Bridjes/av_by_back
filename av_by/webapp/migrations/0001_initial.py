# Generated by Django 5.0 on 2024-03-09 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Марка')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('year', models.CharField(max_length=200, verbose_name='Год')),
                ('body_type', models.CharField(max_length=200, verbose_name='Кузов')),
                ('transmission', models.CharField(max_length=200, verbose_name='Коробка передач')),
                ('engine_type', models.CharField(max_length=200, verbose_name='Тип двигателя')),
                ('drive_unit', models.CharField(max_length=200, verbose_name='Привод')),
                ('engine_volume', models.CharField(max_length=200, verbose_name='Объём двигателя')),
                ('vin', models.CharField(blank=True, default='', max_length=150, verbose_name='VIN')),
                ('state', models.CharField(max_length=100, verbose_name='Состояние')),
                ('mileage', models.IntegerField(verbose_name='Пробег, км')),
                ('color', models.CharField(default='Белый', max_length=200, verbose_name='Цвет')),
                ('interior_material', models.CharField(default='ткань', max_length=100, verbose_name='Материал салона')),
                ('interior_color', models.CharField(default='комби', max_length=100, verbose_name='Цвет салона')),
                ('abs', models.BooleanField(blank=True, default=False, verbose_name='ABS')),
                ('esp', models.BooleanField(blank=True, default=False, verbose_name='ESP')),
                ('anti_slip', models.BooleanField(blank=True, default=False, verbose_name='Антипробуксовочная')),
                ('immobilizer', models.BooleanField(blank=True, default=False, verbose_name='Иммобилайзер')),
                ('alarm_system', models.BooleanField(blank=True, default=False, verbose_name='Сигнализация')),
                ('alloy_wheels', models.BooleanField(blank=True, default=False, verbose_name='Легкосплавные диски')),
                ('roof_rails', models.BooleanField(blank=True, default=False, verbose_name='Рейлинги на крыше')),
                ('trailer_coupling', models.BooleanField(blank=True, default=False, verbose_name='Фаркоп')),
                ('seats', models.BooleanField(blank=True, default=False, verbose_name='Сидений')),
                ('windshield', models.BooleanField(blank=True, default=False, verbose_name='Лобового стекла')),
                ('mirrors', models.BooleanField(blank=True, default=False, verbose_name='Зеркал')),
                ('steering_wheel', models.BooleanField(blank=True, default=False, verbose_name='Руля')),
                ('autonomous_heater', models.BooleanField(blank=True, default=False, verbose_name='Автономный отопитель')),
                ('engine_autorun', models.BooleanField(blank=True, default=False, verbose_name='Автозапуск двигателя')),
                ('cruise_control', models.BooleanField(blank=True, default=False, verbose_name='Круиз-контроль')),
                ('multimedia', models.BooleanField(blank=True, default=False, verbose_name='Управление мультимедиа с руля')),
                ('electric_seat_adjustment', models.BooleanField(blank=True, default=False, verbose_name='Электрорегулировка сидений')),
                ('front_electric_windows', models.BooleanField(blank=True, default=False, verbose_name='Передние электро-стеклоподъёмники')),
                ('rear_electric_windows', models.BooleanField(blank=True, default=False, verbose_name='Задние электро-стеклоподъёмники')),
                ('hatch', models.BooleanField(blank=True, default=False, verbose_name='Люк')),
                ('panoramic_roof', models.BooleanField(blank=True, default=False, verbose_name='Панорамная крыша')),
                ('front_cushions', models.BooleanField(blank=True, default=False, verbose_name='Передние подушки')),
                ('side_cushions', models.BooleanField(blank=True, default=False, verbose_name='Боковые подушки')),
                ('rear_cushions', models.BooleanField(blank=True, default=False, verbose_name='Задние подушки')),
                ('xenon', models.BooleanField(blank=True, default=False, verbose_name='Ксеноновые')),
                ('fog_lights', models.BooleanField(blank=True, default=False, verbose_name='Противотуманные')),
                ('led_lights', models.BooleanField(blank=True, default=False, verbose_name='Светодиодные')),
                ('aux_or_ipod', models.BooleanField(blank=True, default=False, verbose_name='AUX или iPod')),
                ('bluetooth', models.BooleanField(blank=True, default=False, verbose_name='Bluetooth')),
                ('cd_or_mp3', models.BooleanField(blank=True, default=False, verbose_name='CD или MP3')),
                ('usb', models.BooleanField(blank=True, default=False, verbose_name='USB')),
                ('multimedia_screen', models.BooleanField(blank=True, default=False, verbose_name='Мультимедийный экран')),
                ('regular_navigation', models.BooleanField(blank=True, default=False, verbose_name='Штатная навигация')),
                ('rain_sensor', models.BooleanField(blank=True, default=False, verbose_name='Датчик дождя')),
                ('rear_view_camera', models.BooleanField(blank=True, default=False, verbose_name='Камера заднего вида')),
                ('parking_sensors', models.BooleanField(blank=True, default=False, verbose_name='Парктроники')),
                ('monitoring_dead_zones_mirrors', models.BooleanField(blank=True, default=False, verbose_name='Контроль мертвых зон на зеркалах')),
                ('climate_control', models.BooleanField(blank=True, default=False, verbose_name='Климат-контроль')),
                ('conditioner', models.BooleanField(blank=True, default=False, verbose_name='Кондиционер')),
                ('registration_country', models.CharField(blank=True, default='', max_length=100, verbose_name='Страна регистрации')),
                ('accounting', models.CharField(blank=True, default='', max_length=100, verbose_name='Учёт')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='Car', verbose_name='Фото 1')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='Car', verbose_name='Фото 2')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='Car', verbose_name='Фото 3')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='Car', verbose_name='Фото 4')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='Car', verbose_name='Фото 5')),
                ('youtube', models.URLField(blank=True, default='', verbose_name='Видео из YouTube')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('name', models.CharField(blank=True, default='', max_length=200, verbose_name='Имя продавца')),
                ('phone_1', models.CharField(blank=True, default='', max_length=9, verbose_name='Номер телефона 1')),
                ('phone_2', models.CharField(blank=True, default='', max_length=9, verbose_name='Номер телефона 2')),
                ('phone_3', models.CharField(blank=True, default='', max_length=9, verbose_name='Номер телефона 3')),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, создавший запись')),
            ],
            options={
                'verbose_name': 'Легковой автомобиль',
                'verbose_name_plural': 'Легковые авто',
            },
        ),
    ]
