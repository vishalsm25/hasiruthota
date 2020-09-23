from django.contrib import admin
from .models import featured_product, new_product, best_plants


# Register your models here.
admin.site.register(featured_product)
admin.site.register(new_product)
admin.site.register(best_plants)
