# Generated by Django 5.2.1 on 2025-06-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_data', '0010_healthrecord_anti_hcv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthrecord',
            name='absolute_basophil_count',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='absolute_eosinophil_count',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='absolute_immature_granulocyte',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='absolute_lymphocyte_count',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='absolute_monocyte_count',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='absolute_neutrophil_count',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='carbon_dioxide',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='cholesterol_vldl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='immature_granulocyte',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='serum_folate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='urine_albumin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='urine_albumin_creatinine_ratio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='urine_creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='urine_wbc_esterase',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='vitamin_b12',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='vitamin_d',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='urine_urobilinogen',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
