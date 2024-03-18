import logging
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Client, Product, Order
from myapp.forms import ProductForm


logger = logging.getLogger(__name__)

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы можете найти информацию о сайте и обо мне.</p>
    """
    logger.info('Посещена главная страница')
    return render(request, 'myapp/home.html', {'html': html})

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я - разработчик Django-приложений.</p>
    """
    logger.info('Посещена страница "О себе"')
    return render(request, 'myapp/about.html', {'html': html})

def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return JsonResponse({'message': 'Клиент успешно создан'})
        
def get_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return JsonResponse({'name': client.name, 'email': client.email, 'phone_number': client.phone_number, 'address': client.address})

def update_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return JsonResponse({'message': 'Товар успешно обновлен'})


def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return JsonResponse({'message': 'Заказ удален'})

def client_orders_list(request, client_id):
    client_orders_last_7_days = Order.objects.filter(client_id=client_id, created_at__gte=timezone.now()-timezone.timedelta(days=7)).distinct()
    client_orders_last_30_days = Order.objects.filter(client_id=client_id, created_at__gte=timezone.now()-timezone.timedelta(days=30)).distinct()
    client_orders_last_365_days = Order.objects.filter(client_id=client_id, created_at__gte=timezone.now()-timezone.timedelta(days=365)).distinct()
    
    return render(request, 'client_orders_list.html', {'client_orders_last_7_days': client_orders_last_7_days,
                                                        'client_orders_last_30_days': client_orders_last_30_days,
                                                        'client_orders_last_365_days': client_orders_last_365_days})


def upload_product_photo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Обработка загрузки фото продукта
            photo = request.FILES['photo']
            # Дополнительная логика обработки загруженного фото
            return JsonResponse({'message': 'Фото продукта успешно загружено'})
    else:
        form = ProductForm()
    return render(request, 'upload_product_photo.html', {'form': form})

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'client_detail.html', {'client': client})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

def home(request):
    return render(request, 'home.html')

