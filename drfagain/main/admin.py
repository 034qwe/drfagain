from django.contrib import admin

from .models import Animals
from .models import Category_Animals

# Register your models here.

admin.site.register(Animals)
admin.site.register(Category_Animals)