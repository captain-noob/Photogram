# Generated by Django 2.1.5 on 2019-03-24 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_user_detials_report'),
        ('upload', '0002_imguploads_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=1000)),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.user_detials')),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='upload.imguploads')),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.user_detials')),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='upload.imguploads')),
            ],
        ),
    ]
