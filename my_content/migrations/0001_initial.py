# Generated by my_content 4.2.3 on 2023-09-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=32, verbose_name='app label')),
                ('model', models.CharField(max_length=32, verbose_name='model')),
            ],
        ),
    ]
