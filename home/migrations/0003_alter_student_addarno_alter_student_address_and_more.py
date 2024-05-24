# Generated by Django 4.2.11 on 2024-05-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_addarno_teacher_yearsofexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='AddarNo',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='classs',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(max_length=50),
        ),
    ]