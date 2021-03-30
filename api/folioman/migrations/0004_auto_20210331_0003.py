# Generated by Django 3.1.7 on 2021-03-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioman', '0003_auto_20201121_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amc',
            options={'verbose_name': 'AMC', 'verbose_name_plural': 'AMCs'},
        ),
        migrations.AlterModelOptions(
            name='fundcategory',
            options={'verbose_name': 'FundCategory', 'verbose_name_plural': 'Fund Categories'},
        ),
        migrations.AlterModelOptions(
            name='fundscheme',
            options={'verbose_name': 'Fund Scheme', 'verbose_name_plural': 'Fund Schemes'},
        ),
        migrations.RenameField(
            model_name='schemevalue',
            old_name='units',
            new_name='balance',
        ),
        migrations.AddField(
            model_name='schemevalue',
            name='avg_nav',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=30),
        ),
        migrations.AlterUniqueTogether(
            name='foliovalue',
            unique_together={('folio_id', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='portfoliovalue',
            unique_together={('portfolio_id', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='schemevalue',
            unique_together={('scheme_id', 'date')},
        ),
    ]
