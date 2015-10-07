# Third Party Stuff
from django.contrib import admin

from .models import Brand


class BrandAdmin(admin.ModelAdmin):

    '''
    Admin View for Visitor
    '''
    list_display = ('name_of_the_brand', 'image', 'phone_number')
    list_filter = ('created', )
    search_fields = ['name_of_the_brand', ]

    def image(self, obj):
        if obj.photo:
            return '<img src="%s"/>' % obj.photo.thumbnail['100x100'].url
        return '(None)'
    image.allow_tags = True

admin.site.register(Brand, BrandAdmin)
