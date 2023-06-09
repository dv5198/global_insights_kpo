# Generated by Django 4.1.7 on 2023-04-10 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0002_warranty_details_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warranty_details',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='warranty_details',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='warranty_details',
            name='purchase_place',
        ),
        migrations.RemoveField(
            model_name='warranty_details',
            name='purchase_proof',
        ),
        migrations.RemoveField(
            model_name='warranty_details',
            name='warranty_date',
        ),
        migrations.AddField(
            model_name='warranty_details',
            name='brand_category',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warranty_details',
            name='date_of_delivery',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warranty_details',
            name='date_of_purchase',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warranty_details',
            name='place_of_purchase',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warranty_details',
            name='proof_of_purchase',
            field=models.FileField(default=django.utils.timezone.now, upload_to='proof_of_purchase/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warranty_details',
            name='warranty_valid_till',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warranty_details',
            name='delivery_order',
            field=models.FileField(upload_to='delivery_order/'),
        ),
        migrations.AlterField(
            model_name='warranty_details',
            name='model_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='warranty_details',
            name='serial_number',
            field=models.CharField(max_length=100),
        ),
    ]
