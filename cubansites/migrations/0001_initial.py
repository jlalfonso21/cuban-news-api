from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='WebCrawler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('file_dir', models.FileField(upload_to='spiders/uploaded', verbose_name='File')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('url', models.URLField(verbose_name='URL')),
                ('categories', models.ManyToManyField(related_name='websites', to='cubansites.Category', verbose_name='Categories')),
            ],
        ),
        migrations.CreateModel(
            name='RssFeedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('feed_type', models.CharField(choices=[('rss', 'RSS'), ('atom', 'ATOM')], default='rss', max_length=32, verbose_name='Type')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cubansites.category', verbose_name='Category')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cubansites.website', verbose_name='Website')),
            ],
        ),
    ]
