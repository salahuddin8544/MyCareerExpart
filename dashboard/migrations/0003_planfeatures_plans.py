# Generated by Django 4.2 on 2024-03-31 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_company_jobtype_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('features', models.ManyToManyField(blank=True, to='dashboard.planfeatures')),
            ],
        ),
    ]
