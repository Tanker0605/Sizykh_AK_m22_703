# Generated by Django 4.2.6 on 2023-11-11 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={
                "ordering": ["last_name"],
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={
                "ordering": ["name"],
                "verbose_name": "Блюдо",
                "verbose_name_plural": "Блюда",
            },
        ),
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["-date_time"],
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
        migrations.AlterModelOptions(
            name="orderitem",
            options={
                "ordering": ["-id"],
                "verbose_name": "Элемент заказа",
                "verbose_name_plural": "Элементы заказов",
            },
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="client",
            name="address",
            field=models.CharField(max_length=255, verbose_name="Адрес"),
        ),
        migrations.AlterField(
            model_name="client",
            name="first_name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="client",
            name="last_name",
            field=models.CharField(max_length=100, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone",
            field=models.CharField(max_length=100, verbose_name="Номер телефона"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="calories",
            field=models.PositiveIntegerField(verbose_name="Калории"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=8, verbose_name="Цена"
            ),
        ),
        migrations.AlterField(
            model_name="dish",
            name="weight",
            field=models.PositiveIntegerField(verbose_name="Вес"),
        ),
        migrations.AlterField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="date_time",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="Дата"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="dish",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.dish",
                verbose_name="Блюдо",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.order",
                verbose_name="Заказ",
            ),
        ),
    ]
