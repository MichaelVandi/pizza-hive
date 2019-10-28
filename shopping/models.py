from django.db import models

# Create your models here.

# Creating an object of menu item
class Item(models.Model):
    # Initializing attributes of the item
    name = models.CharField(max_length = 60, blank = False)
    category = models.CharField(max_length = 60, blank = False)
    image = models.ImageField(blank = False, null = False)
    has_size = models.BooleanField()
    has_topping = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.category}"

class Topping(models.Model):
    name = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

# Decided to separate Subs into it's own table because there are so many differences between subs and regular
# Food items: Like not all toppings can be applied to a specific sub

class Sub(models.Model):
    name = models.CharField(max_length = 60, blank = False)
    image = models.ImageField(blank = False, null = False)
    has_topping = models.BooleanField()
    available_toppings_comma = models.TextField(max_length = 120, blank=True, )
    price_small = models.FloatField(blank = False, null = False)
    price_large = models.FloatField(blank = False, null = False)

    def __str__(self):
        return f"{self.name}"

# Making price a model because it also has attributes that apply to only specific items
# Like: some items have only one size some come in small and large sizes
class Item_price_by_size(models.Model):
    name = models.ForeignKey(Item, blank = False, null = False, on_delete=models.CASCADE)
    price_small = models.FloatField(blank = False, null = False)
    price_large = models.FloatField(blank = False, null = False)

    def __str__(self):
        return f"{self.name} Small: {self.price_small} Large: {self.price_large}"
    
class Item_price_no_size(models.Model):
    name = models.ForeignKey(Item, blank = False, null = False, on_delete=models.CASCADE)
    price = models.FloatField(blank = False, null = False)

    def __str__(self):
        return f"{self.name} {self.price}"
class Orders(models.Model):
    username=models.CharField(max_length = 60, blank = False)
    name = models.CharField(max_length = 80, blank = False)
    items=models.TextField(blank = False)
    total_amount = models.FloatField(blank = False, null = False)

    
    