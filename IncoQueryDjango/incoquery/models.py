from django.db import models
from django import forms

class IncoqueryQuery(models.Model):

    ## TODO IMPLEMENTAR DJANDO EAD
    pais_estudio_list = (
        ("CR", "Costa Rica"),
        ("ECU", "Ecuador"),
        ("VEN", "Venezuela"),
        ("PAN", "Panama")
    )
    regimen_list = (
        ("EX", "Exportacion"),
        ("IM", "Importacion")
    )
    sectores_list = (
        ('ANI','Animales y Productos Animales'),
        ('CAL','Calzado / Sombreros'),
        ('CUE','Cuero sin curtir, pieles, cuero y pelajes'),
        ('DIV','Diversos'),
        ('MAD','Madera y productos de madera'),
        ('MAQ','Maquinaria / Electrica'),
        ('MET','Metales'),
        ('ND','No hay datos'),
        ('PIE','Piedras / Vidrio'),
        ('PLA','Plasticos / Hules'),
        ('ALI','Productos Alimenticios'),
        ('MIN','Productos Minerales'),
        ('QUI','Productos Quimicos y conexos'),
        ('VEG','Productos Vegetales'),
        ('TEX','Textiles'),
        ('TRA','Transporte')
    )
    pais_estudio = models.CharField(max_length=3, choices=pais_estudio_list, default="CR")
    regimen = models.CharField(max_length=2, choices=regimen_list, default="EX")
    rango_desde = models.DateField(null=True, auto_now=True)
    rango_hasta = models.DateField(null = True, auto_now=True)
    trader_name = models.CharField(max_length=2000, blank = True, verbose_name="Username")
    hs_code = models.CharField(max_length=2000, blank = True)
    departure_country = models.CharField(max_length=2000, blank = True)
    origin_country = models.CharField(max_length=2000, blank = True)
    sector = models.CharField(max_length=3, choices=sectores_list, default="ANI")
    destiny_country = models.CharField(max_length=2000, blank = True)
    transport_mode = models.CharField(max_length=2000, blank = True)
    acquisition_country = models.CharField(max_length=2000, blank = True)
    customs_name = models.CharField(max_length=2000, blank = True)
    declaration_no = models.CharField(max_length=2000, blank = True)
    cargo_description = models.CharField(max_length=2000, blank = True)
    mes_periodo = models.CharField(max_length=2000, blank = True)
    transport_company = models.CharField(max_length=2000, blank = True)
    transport_company_id = models.CharField(max_length=2000, blank = True)
    arrival_date = models.CharField(max_length=2000, blank = True)
    destinan_wrhouse_name = models.CharField(max_length=2000, blank = True)
    registry_date = models.CharField(max_length=2000, blank = True)
    trader_address = models.CharField(max_length=2000, blank = True)
    declarant_name = models.CharField(max_length=2000, blank = True)
    cust_entry_exit = models.CharField(max_length=2000, blank = True)
    tax_id_declarant = models.CharField(max_length=2000, blank = True)
    tax_id_trader = models.CharField(max_length=2000, blank = True)
    warehouse_name = models.CharField(max_length=2000, blank = True)
    registry_name = models.CharField(max_length=2000, blank = True)
    ownership_trader = models.CharField(max_length=2000, blank = True)
    destinan_cust = models.CharField(max_length=2000, blank = True)
    release_desc = models.CharField(max_length=2000, blank = True)
    package_type = models.CharField(max_length=2000, blank = True)
    total_guarantee_value = models.CharField(max_length=2000, blank = True)
    no_of_packages = models.CharField(max_length=2000, blank = True)
    operation_name = models.CharField(max_length=2000, blank = True)
    currency_descr = models.CharField(max_length=2000, blank = True)
    manifest_number = models.CharField(max_length=2000, blank = True)
    registry_hour = models.CharField(max_length=2000, blank = True)
    shipping_marks = models.CharField(max_length=2000, blank = True)
    ship_name = models.CharField(max_length=2000, blank = True)
    bl_number = models.CharField(max_length=2000, blank = True)
    declaration_type = models.CharField(max_length=2000, blank = True)
    remarks = models.CharField(max_length=2000, blank = True)
    release_form = models.CharField(max_length=2000, blank = True)
    ownership_agent = models.CharField(max_length=2000, blank = True)
    line_number = models.CharField(max_length=2000, blank = True)
    ship_registry = models.CharField(max_length=2000, blank = True)
    exchange_rate = models.CharField(max_length=2000, blank = True)
    guarantee_number = models.CharField(max_length=2000, blank = True)
    operation_code = models.CharField(max_length=2000, blank = True)
    release_channel = models.CharField(max_length=2000, blank = True)
    shipping_number = models.CharField(max_length=2000, blank = True)
    serial_number = models.CharField(max_length=2000, blank = True)



