from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='surname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
