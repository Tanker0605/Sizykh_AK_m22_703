from django.contrib import admin

from .models import Client, Dish, Order, OrderItem

class clientadmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name','phone')
  search_fields  = ('first_name', 'last_name','phone')

class dishadmin(admin.ModelAdmin):
  list_display = ('name','weight','calories','price')
  search_fields = ('name','weight','calories','price')


class orderadmin(admin.ModelAdmin):
  list_display = ('id','client','date_time' )
  search_fields = ('id','client','date_time' )

class itemadmin(admin.ModelAdmin):
  list_display = ('order','dish','quantity' )
  list_filter = ('order','dish','quantity'  )

admin.site.register(Client,clientadmin)
admin.site.register(Dish,dishadmin)
admin.site.register(Order,orderadmin)
admin.site.register(OrderItem,itemadmin)


# Register your models here.
