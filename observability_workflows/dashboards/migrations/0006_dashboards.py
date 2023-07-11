# Generated by Django 3.2.5 on 2023-07-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0005_auto_20230613_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date of creation')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Retired', 'Retired')], max_length=50)),
                ('dashboard_type', models.CharField(choices=[('Custom', 'Custom'), ('External', 'External')], max_length=50)),
            ],
        ),
    ]