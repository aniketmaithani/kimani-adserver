# Third Party Stuff
from django.contrib import admin

from .models import Coupon


class CouponAdmin(admin.ModelAdmin):

    '''
    Admin View for Visitor
    '''
    list_display = ('coupon_name', 'photo_of_the_coupon', )
    list_filter = ('created', )
    search_fields = ['name_of_the_brand', ]

    def image(self, obj):
        if obj.photo_of_the_coupon:
            return '<img src="%s"/>' % obj.photo_of_the_coupon.thumbnail['100x100'].url
        return '(None)'
    image.allow_tags = True

admin.site.register(Coupon, CouponAdmin)
