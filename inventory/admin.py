from django.contrib import admin

from .models import Drinks_Inventory,Items

class ItemAdminInline(admin.TabularInline):
    model = Items
    fields = ['name','quantity','expiry']
    extra = 0
@admin.register(Drinks_Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','location']
    inlines = [ItemAdminInline]

#class ItemAdmin(admin.ModelAdmin):
 #   list_display = ['Drinks_Inventory','name','quantity','expiry']

#admin.site.register(Drinks_Inventory,InventoryAdmin)
#admin.site.register(Items,ItemAdmin)
