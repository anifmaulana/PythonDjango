# Generated by Django 2.1.3 on 2018-11-13 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customers_rel_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers_rel_loan',
            name='loanid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Loan'),
        ),
    ]
