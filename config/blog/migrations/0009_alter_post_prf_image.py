# Generated by Django 5.0.1 on 2024-01-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_prf_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PRF_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='photo/%Y/%m/%d'),
        ),
    ]
