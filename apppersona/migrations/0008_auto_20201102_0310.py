# Generated by Django 2.2.16 on 2020-11-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppersona', '0007_auto_20201102_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='region',
            field=models.CharField(choices=[('primera', 'I Región de Tarapacá'), ('segunda', 'II Región de Antofagasta'), ('tercera', 'III Región de Atacama'), ('cuarta', 'IV Región de Coquimbo'), ('quinta', 'V Región de Valparaíso'), ('sexta', 'VI Región del Libertador General Bernardo O’Higgins'), ('septima', 'VII Región del Maule'), ('octava', 'VIII Región del Biobío'), ('novena', 'IX Región de La Araucanía'), ('decima', 'X Región de Los Lagos'), ('decimoprimera', 'XI Región Aysén del General Carlos Ibáñez del Campo'), ('decimosegunda', 'XII Región de Magallanes y Antártica Chilena'), ('Region Metropolitana', 'Región Metropolitana de Santiago'), ('decimocuarta', 'XIV Región de Los Ríos'), ('decimoquinta', 'XV Región de Arica y Parinacota'), ('decimosexta', 'XVI Región de Ñuble')], default='Region Metropolitana', max_length=6),
        ),
    ]
