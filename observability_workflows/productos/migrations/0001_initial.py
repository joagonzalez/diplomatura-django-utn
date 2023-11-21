# Generated by Django 3.2.5 on 2023-10-13 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Retired', 'Retired')], default='Draft', max_length=10)),
                ('product', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(verbose_name='Publish Date')),
                ('image', models.ImageField(blank=True, null=True, upload_to='producto/%Y/%m/%d')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.category')),
            ],
        ),
    ]
