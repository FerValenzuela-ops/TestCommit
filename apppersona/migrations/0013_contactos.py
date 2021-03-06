# Generated by Django 2.2.16 on 2020-11-03 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppersona', '0012_persona_edad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('asunto', models.TextField(max_length=50)),
                ('telefono', models.IntegerField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('mensaje', models.TextField(max_length=50)),
            ],
        ),
    ]
