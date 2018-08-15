# Generated by Django 2.1 on 2018-08-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20180815_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gugun',
            options={'verbose_name_plural': ' 구/군 테이블'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id'], 'verbose_name_plural': '   프로젝트 테이블'},
        ),
        migrations.AlterModelOptions(
            name='projectapply',
            options={'verbose_name_plural': '   프로젝트 지원 테이블'},
        ),
        migrations.AlterModelOptions(
            name='projecttag',
            options={'verbose_name_plural': '  프로젝트별 태그 테이블'},
        ),
        migrations.AlterModelOptions(
            name='sido',
            options={'verbose_name_plural': ' 시/도 테이블'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '  태그 테이블'},
        ),
        migrations.AlterUniqueTogether(
            name='projecttag',
            unique_together={('project', 'tag')},
        ),
    ]
