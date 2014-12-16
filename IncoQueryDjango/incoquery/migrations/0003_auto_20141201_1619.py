# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incoquery', '0002_auto_20141124_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncoqueryQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais_estudio', models.CharField(default=b'CR', max_length=3, choices=[(b'CR', b'Costa Rica'), (b'ECU', b'Ecuador'), (b'VEN', b'Venezuela'), (b'PAN', b'Panama')])),
                ('regimen', models.CharField(default=b'EX', max_length=2, choices=[(b'EX', b'Exportacion'), (b'IM', b'Importacion')])),
                ('rango_desde', models.DateField(auto_now=True, null=True)),
                ('rango_hasta', models.DateField(auto_now=True, null=True)),
                ('trader_name', models.CharField(max_length=2000, verbose_name=b'Username', blank=True)),
                ('hs_code', models.CharField(max_length=2000, blank=True)),
                ('departure_country', models.CharField(max_length=2000, blank=True)),
                ('origin_country', models.CharField(max_length=2000, blank=True)),
                ('sector', models.CharField(default=b'ANI', max_length=3, choices=[(b'ANI', b'Animales y Productos Animales'), (b'CAL', b'Calzado / Sombreros'), (b'CUE', b'Cuero sin curtir, pieles, cuero y pelajes'), (b'DIV', b'Diversos'), (b'MAD', b'Madera y productos de madera'), (b'MAQ', b'Maquinaria / Electrica'), (b'MET', b'Metales'), (b'ND', b'No hay datos'), (b'PIE', b'Piedras / Vidrio'), (b'PLA', b'Plasticos / Hules'), (b'ALI', b'Productos Alimenticios'), (b'MIN', b'Productos Minerales'), (b'QUI', b'Productos Quimicos y conexos'), (b'VEG', b'Productos Vegetales'), (b'TEX', b'Textiles'), (b'TRA', b'Transporte')])),
                ('destiny_country', models.CharField(max_length=2000, blank=True)),
                ('transport_mode', models.CharField(max_length=2000, blank=True)),
                ('acquisition_country', models.CharField(max_length=2000, blank=True)),
                ('customs_name', models.CharField(max_length=2000, blank=True)),
                ('declaration_no', models.CharField(max_length=2000, blank=True)),
                ('cargo_description', models.CharField(max_length=2000, blank=True)),
                ('mes_periodo', models.CharField(max_length=2000, blank=True)),
                ('transport_company', models.CharField(max_length=2000, blank=True)),
                ('transport_company_id', models.CharField(max_length=2000, blank=True)),
                ('arrival_date', models.CharField(max_length=2000, blank=True)),
                ('destinan_wrhouse_name', models.CharField(max_length=2000, blank=True)),
                ('registry_date', models.CharField(max_length=2000, blank=True)),
                ('trader_address', models.CharField(max_length=2000, blank=True)),
                ('declarant_name', models.CharField(max_length=2000, blank=True)),
                ('cust_entry_exit', models.CharField(max_length=2000, blank=True)),
                ('tax_id_declarant', models.CharField(max_length=2000, blank=True)),
                ('tax_id_trader', models.CharField(max_length=2000, blank=True)),
                ('warehouse_name', models.CharField(max_length=2000, blank=True)),
                ('registry_name', models.CharField(max_length=2000, blank=True)),
                ('ownership_trader', models.CharField(max_length=2000, blank=True)),
                ('destinan_cust', models.CharField(max_length=2000, blank=True)),
                ('release_desc', models.CharField(max_length=2000, blank=True)),
                ('package_type', models.CharField(max_length=2000, blank=True)),
                ('total_guarantee_value', models.CharField(max_length=2000, blank=True)),
                ('no_of_packages', models.CharField(max_length=2000, blank=True)),
                ('operation_name', models.CharField(max_length=2000, blank=True)),
                ('currency_descr', models.CharField(max_length=2000, blank=True)),
                ('manifest_number', models.CharField(max_length=2000, blank=True)),
                ('registry_hour', models.CharField(max_length=2000, blank=True)),
                ('shipping_marks', models.CharField(max_length=2000, blank=True)),
                ('ship_name', models.CharField(max_length=2000, blank=True)),
                ('bl_number', models.CharField(max_length=2000, blank=True)),
                ('declaration_type', models.CharField(max_length=2000, blank=True)),
                ('remarks', models.CharField(max_length=2000, blank=True)),
                ('release_form', models.CharField(max_length=2000, blank=True)),
                ('ownership_agent', models.CharField(max_length=2000, blank=True)),
                ('line_number', models.CharField(max_length=2000, blank=True)),
                ('ship_registry', models.CharField(max_length=2000, blank=True)),
                ('exchange_rate', models.CharField(max_length=2000, blank=True)),
                ('guarantee_number', models.CharField(max_length=2000, blank=True)),
                ('operation_code', models.CharField(max_length=2000, blank=True)),
                ('release_channel', models.CharField(max_length=2000, blank=True)),
                ('shipping_number', models.CharField(max_length=2000, blank=True)),
                ('serial_number', models.CharField(max_length=2000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='incoquery_query',
        ),
    ]
