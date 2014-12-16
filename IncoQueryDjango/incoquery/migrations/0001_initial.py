# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='incoquery_query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais_estudio', models.CharField(max_length=255)),
                ('regimen', models.CharField(max_length=255)),
                ('rango_desde', models.DateField()),
                ('rango_hasta', models.DateField()),
                ('trader_name', models.CharField(max_length=255)),
                ('hs_code', models.IntegerField()),
                ('departure_country', models.CharField(max_length=255)),
                ('origin_country', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('destiny_country', models.CharField(max_length=255)),
                ('transport_mode', models.CharField(max_length=255)),
                ('acquisition_country', models.CharField(max_length=255)),
                ('customs_name', models.CharField(max_length=255)),
                ('declaration_no', models.CharField(max_length=255)),
                ('cargo_description', models.CharField(max_length=255)),
                ('mes_periodo', models.CharField(max_length=255)),
                ('transport_company', models.CharField(max_length=255)),
                ('transport_company_id', models.CharField(max_length=255)),
                ('arrival_date', models.CharField(max_length=255)),
                ('destinan_wrhouse_name', models.CharField(max_length=255)),
                ('registry_date', models.CharField(max_length=255)),
                ('trader_address', models.CharField(max_length=255)),
                ('declarant_name', models.CharField(max_length=255)),
                ('cust_entry_exit', models.CharField(max_length=255)),
                ('tax_id_declarant', models.CharField(max_length=255)),
                ('tax_id_trader', models.CharField(max_length=255)),
                ('warehouse_name', models.CharField(max_length=255)),
                ('registry_name', models.CharField(max_length=255)),
                ('ownership_trader', models.CharField(max_length=255)),
                ('destinan_cust', models.CharField(max_length=255)),
                ('release_desc', models.CharField(max_length=255)),
                ('package_type', models.CharField(max_length=255)),
                ('total_guarantee_value', models.CharField(max_length=255)),
                ('no_of_packages', models.CharField(max_length=255)),
                ('operation_name', models.CharField(max_length=255)),
                ('currency_descr', models.CharField(max_length=255)),
                ('manifest_number', models.CharField(max_length=255)),
                ('registry_hour', models.CharField(max_length=255)),
                ('shipping_marks', models.CharField(max_length=255)),
                ('ship_name', models.CharField(max_length=255)),
                ('bl_number', models.CharField(max_length=255)),
                ('declaration_type', models.CharField(max_length=255)),
                ('remarks', models.CharField(max_length=255)),
                ('release_form', models.CharField(max_length=255)),
                ('ownership_agent', models.CharField(max_length=255)),
                ('line_number', models.CharField(max_length=255)),
                ('ship_registry', models.CharField(max_length=255)),
                ('exchange_rate', models.CharField(max_length=255)),
                ('guarantee_number', models.CharField(max_length=255)),
                ('operation_code', models.CharField(max_length=255)),
                ('release_channel', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=255)),
                ('shipping_number', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
