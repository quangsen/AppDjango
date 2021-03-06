# Generated by Django 2.2.1 on 2019-05-14 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodball', '0002_auto_20190513_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodball.Group')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='shirt_size',
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodball.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='foodball.Membership', to='foodball.Person'),
        ),
    ]
