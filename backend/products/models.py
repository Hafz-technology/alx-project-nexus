from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="وصف المنتج")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج")
    stock = models.IntegerField(default=0, verbose_name="الكمية المتاحة")
    
    # الأسعار الخليجية المخصصة
    price_sar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر بالريال السعودي")
    price_aed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر بالدرهم الإماراتي", blank=True, null=True)
    price_kwd = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="السعر بالدينار الكويتي", blank=True, null=True)
    price_bhd = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="السعر بالدينار البحريني", blank=True, null=True)
    price_omr = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="السعر بالريال العماني", blank=True, null=True)
    price_qar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر بالريال القطري", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    PAYMENT_METHODS = [('ONLINE', 'دفع إلكتروني'), ('COD', 'دفع عند الاستلام')]
    STATUS_CHOICES = [('PENDING', 'انتظار'), ('PAID', 'تم الدفع'), ('SHIPPED', 'شحن'), ('DELIVERED', 'تم')]

    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='SAR')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='ONLINE')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
    
    
    
    
    