from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('registration_date',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('order_set')  

    def order_count(self, obj):
        return obj.order_set.count()  
    
    order_count.short_description = 'Number of orders'  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'quantity', 'added_date', 'formatted_price')  # Добавляем форматированное поле цены
    search_fields = ('name', 'description')
    list_filter = ('added_date',)  

    def formatted_price(self, obj):
        return f'${obj.price}'  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date', 'product_list')
    search_fields = ('client__name', 'total_amount')
    list_filter = ('order_date',)

    def product_list(self, obj):
        return ", ".join([product.name for product in obj.products.all()])  

    product_list.short_description = 'Products in order'  
