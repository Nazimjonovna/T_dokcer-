# Generated by Django 5.0 on 2023-12-18 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('about', models.TextField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('cost', models.IntegerField(null=True)),
                ('category', models.CharField(choices=[('Elektronika', 'Elektronika'), ('Maishiy_texnika', 'Maishiy_texnika'), ('Noutbooklar', 'Noutbooklar'), ('Smartfonlar', 'Smartfonlar'), ('Planshetlar', 'Planshetlar')], max_length=250, null=True)),
                ('color', models.CharField(max_length=13, null=True)),
                ('image', models.ImageField(null=True, upload_to='rasmlar/')),
                ('time', models.DateTimeField(auto_now=True)),
                ('prosent', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.admin')),
            ],
        ),
    ]
