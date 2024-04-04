from django.contrib import admin
from inventario.models import Carro

class InventarioAdmin(admin.ModelAdmin):
    list_display= ["marca","cantidad","pais"]
    list_search= ["marca"]

admin.site.register(Carro,InventarioAdmin)