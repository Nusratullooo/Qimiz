from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilingan')], default='New', max_length=20)),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
