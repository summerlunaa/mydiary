# Generated by Django 3.1.7 on 2021-03-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0002_content_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='content',
            name='today_exercise',
            field=models.CharField(choices=[('쉬었어요', '쉬었어요'), ('하체', '하체'), ('팔', '팔'), ('등', '등'), ('복근', '복근'), ('가슴', '가슴'), ('어깨', '어깨')], default='쉬었어요', max_length=5),
        ),
    ]
