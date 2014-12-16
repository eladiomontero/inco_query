# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incoquery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoquery_query',
            name='acquisition_country',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='arrival_date',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='bl_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='cargo_description',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='currency_descr',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='cust_entry_exit',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='customs_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='declarant_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='declaration_no',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='declaration_type',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='departure_country',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='destinan_cust',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='destinan_wrhouse_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='destiny_country',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='exchange_rate',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='guarantee_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='hs_code',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='line_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='manifest_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='mes_periodo',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='no_of_packages',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='operation_code',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='operation_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='origin_country',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='ownership_agent',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='ownership_trader',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='package_type',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='pais_estudio',
            field=models.CharField(default=b'CR', max_length=3, choices=[(b'CR', b'Costa Rica'), (b'ECU', b'Ecuador'), (b'VEN', b'Venezuela'), (b'PAN', b'Panama')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='rango_desde',
            field=models.DateField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='rango_hasta',
            field=models.DateField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='regimen',
            field=models.CharField(default=b'EX', max_length=2, choices=[(b'EX', b'Exportacion'), (b'IM', b'Importacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='registry_date',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='registry_hour',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='registry_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='release_channel',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='release_desc',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='release_form',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='remarks',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='sector',
            field=models.CharField(default=b'ANI', max_length=3, choices=[(b'ANI', b'Animales y Productos Animales'), (b'CAL', b'Calzado / Sombreros'), (b'CUE', b'Cuero sin curtir, pieles, cuero y pelajes'), (b'DIV', b'Diversos'), (b'MAD', b'Madera y productos de madera'), (b'MAQ', b'Maquinaria / Electrica'), (b'MET', b'Metales'), (b'ND', b'No hay datos'), (b'PIE', b'Piedras / Vidrio'), (b'PLA', b'Plasticos / Hules'), (b'ALI', b'Productos Alimenticios'), (b'MIN', b'Productos Minerales'), (b'QUI', b'Productos Quimicos y conexos'), (b'VEG', b'Productos Vegetales'), (b'TEX', b'Textiles'), (b'TRA', b'Transporte')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='serial_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='ship_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='ship_registry',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='shipping_marks',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='shipping_number',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='tax_id_declarant',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='tax_id_trader',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='total_guarantee_value',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='trader_address',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='trader_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='transport_company',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='transport_company_id',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='transport_mode',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incoquery_query',
            name='warehouse_name',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
