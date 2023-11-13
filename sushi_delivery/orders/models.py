from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name  = models.CharField(max_length=100, verbose_name='Фамилия')
    email      = models.EmailField()
    phone      = models.CharField(max_length=100, verbose_name='Номер телефона')
    address    = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['last_name']

class Dish(models.Model):
    name      = models.CharField(max_length=100, verbose_name='Название блюда')
    weight    = models.PositiveIntegerField(verbose_name='Вес, гр.')
    calories  = models.PositiveIntegerField(verbose_name='Калории')
    price     = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Цена, руб.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Блюда'
        verbose_name = 'Блюдо'
        ordering = ['name']

class Order(models.Model):
    id 
    client    = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    date_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')

    def __str__(self):
        return f"{self.client.last_name} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"
        
    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-date_time']

class OrderItem(models.Model):

    order    = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    dish     = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Блюдо')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.order.client.last_name} - {self.order.date_time.strftime('%Y-%m-%d %H:%M')}: {self.dish}"

    class Meta:
        verbose_name_plural = 'Элементы заказов'
        verbose_name = 'Элемент заказа'
        ordering = ['-id']