# Generated by Django 5.0.7 on 2024-07-22 15:38

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usersApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='articles/')),
                ('category', models.CharField(choices=[('sustainability', 'Sustainability'), ('product_review', 'Product Review'), ('industry_news', 'Industry News')], default='sustainability', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')], default='Pending', max_length=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcubeApp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('method', models.CharField(default='Unknown', max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('full_name', models.CharField(default='John Doe', max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('address', models.CharField(default='123 Default St', max_length=255)),
                ('city', models.CharField(default='Default City', max_length=100)),
                ('state', models.CharField(default='Default State', max_length=100)),
                ('zip_code', models.CharField(default='00000', max_length=20)),
                ('name_on_card', models.CharField(default='John Doe', max_length=100)),
                ('card_number', models.CharField(default='0000000000000000', max_length=20)),
                ('exp_month', models.CharField(default='01', max_length=2)),
                ('exp_year', models.CharField(default='2025', max_length=4)),
                ('cvv', models.CharField(default='000', max_length=4)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcubeApp.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
