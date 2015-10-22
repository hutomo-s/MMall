# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20151022_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product_id',
            field=models.ForeignKey(to='ecommerce.Product'),
        ),
    ]
