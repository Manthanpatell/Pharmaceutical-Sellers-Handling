from django.contrib import admin
from .models import StoreDetails,ProductDetails,SalesDetails,StockDetails,profilemodel,SK_Bills

#================Admin=========>
from .models import adminregi,SaleFilter
#<==============================

class StoreDetailsAdmin(admin.ModelAdmin):
    list_display = ['StoreName','email','password']

admin.site.register(StoreDetails,StoreDetailsAdmin)
admin.site.register(ProductDetails)
admin.site.register(SalesDetails)
admin.site.register(StockDetails)

#=================Admin===========>
admin.site.register(adminregi)
admin.site.register(SK_Bills)

admin.site.site_header = 'Pharmacist organization Stock Panel'                
admin.site.index_title = '  Admin Panel'         
admin.site.site_title = 'Pharmacist organization Stock Panel'
