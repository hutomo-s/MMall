# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20151022_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='payment_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
