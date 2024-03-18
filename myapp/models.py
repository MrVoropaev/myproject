from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')  # Поле для изображения
    quantity = models.IntegerField()
    added_date = models.DateField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'{self.client} - {self.product}'

    def get_client_name(self):
        return self.client.name

    def get_product_name(self):
        return self.product.name

    
def __str__(self):
    return f"{self.client.name} - - {self.total_price}"