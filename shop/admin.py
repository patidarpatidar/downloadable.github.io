from django.contrib import admin
from shop.models import ProductImages , Product , User ,Payment
from django.utils.html import format_html

from shop.views.payment import API


class ProductImageModel(admin.StackedInline):
    model = ProductImages

class ProductModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'get_description' , 'get_price' , 'get_discount','get_sale_price' , 'file' , 'get_thumbnail' ]
    # inline mtlb productImageModal ko isi table me add krne ke liye yhi se data feel kr sakte hai
    inlines = [ProductImageModel]

    # table me image ke url ko n dikhakr image ko show kr sakte hai
    def get_thumbnail(self , obj):
        return format_html(f'''
         <img height=50px src='{obj.thumbnail.url}'/>
        ''')

    def get_sale_price(self , obj):
        return ( (obj.price) - (obj.price * (obj.discount/100) ) )

    def get_description(self , obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:15] }...</span>')

    def get_price(self , obj):
        return '₹' + str(obj.price)


    def get_discount(self , obj):
        return  str(obj.discount) + '%'

   # short name se table me dikane ke liye
    get_sale_price.short_description = "sale_Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"
    get_description.short_description = "Description"

class UserModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' ,'phone' ,'active' ]

    # table me colm pr click krne pr short ho jayega
    sortable_by = ['id' , 'name']
    # isse direct edit kr sakte hai
    list_editable = ['active']

class PaymentModel(admin.ModelAdmin):
    list_display = ['id' ,
                    'get_user' ,
                    'get_product' ,
                    'get_status' ,
                    'amount' ]

    def amount(self , obj):
        return obj.paymentDetails['payment_request']['amount']
    def get_status(self , obj):
        response = API.payment_request_payment_status(
            obj.payment_request_id , obj.payment_id )

        obj.paymentDetails = response
        if obj.status != "Failed":
            return True
        else:
            return False

     # user name pr click krne pr user se related sari information dikh jayegi
    def get_user(self , obj):
        return format_html(f'<a target="_blank" href="/admin/shop/user/{obj.user.id}">{obj.user}</a>')

    # product name pr click krne pr product se related sari information dikh jayegi
    def get_product(self , obj):
        return format_html(f'<a target="_blank" href="/admin/shop/product/{obj.product.id}">{obj.product}</a>')
    get_user.short_description = 'user'
    get_product.short_description ='product'

    get_status.short_description = 'status'
    get_status.boolean = True



admin.site.register(Product , ProductModel )
admin.site.register(User , UserModel)
admin.site.register(Payment ,PaymentModel)