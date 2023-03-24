from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=300)
    Discount = models.FloatField()



class Prouduct(models.Model):
    title = models.CharField(max_length=244)
    description = models.CharField(max_length=244)
    price = models.DecimalField(max_digits=8, decimal_places=4)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    promotions = models.ManyToManyField(Promotion)


class Collection(models.Model):
    title = models.CharField(max_length=244)
    featured_product = models.ForeignKey('Prouduct', on_delete=models.CASCADE,  related_query_name='+')



class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'B'),
        (MEMBERSHIP_SILVER, 'S'),
        (MEMBERSHIP_GOLD, 'G'),
    ]


    first_name = models.CharField(max_length=244)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=244)
    birth_date = models.DateField()
    membership_choices = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')



class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILD = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING , 'P'),
        (PAYMENT_COMPLETE ,'C'),
        (PAYMENT_FAILD , 'F')
    ]

    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)




class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)





class OrderItem(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Prouduct, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product = models.ForeignKey(Prouduct, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()














