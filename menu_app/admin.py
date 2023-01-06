from django.contrib import admin

# Register your models here.
from .models import *

class tabelmenu_admin(admin.ModelAdmin):
    list_display = ["jenis_id","paket","harga","gambar"]
    search_fields = ["no","paket","harga"]
    list_filter = ["jenis_id"]
    list_per_page = 4
    
admin.site.register(Menu, tabelmenu_admin)
admin.site.register(Jenis)