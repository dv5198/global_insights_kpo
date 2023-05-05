from django.db import models
from django.contrib.auth.models import AbstractUser


paid = "paid"
unpaid = "unpaid"

STATUS = ((paid, "paid"), (unpaid, "unpaid"))

# Create your models here.
class User_Details(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True, default="Username"
    )
    title = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    phone_no = models.CharField(max_length=10, default="123-456-789")
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Warranty_Details(models.Model):

    user = models.OneToOneField(User_Details, on_delete=models.CASCADE)
    product = models.CharField(max_length=10, null=False, blank=False, default="test")
    brand_category = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    place_of_purchase = models.CharField(max_length=100)
    proof_of_purchase = models.FileField(upload_to="proof_of_purchase/")
    date_of_delivery = models.DateField()
    warranty_valid_till = models.DateField()
    delivery_order = models.FileField(upload_to="delivery_order/")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand_category} - {self.serial_number}"


# class Warranty_Subscription(models.Model):
#     user = models.OneToOneField(User_Details, on_delete=models.CASCADE)
#     subscription_status = models.CharField(choices=STATUS, max_length=100)

#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user
