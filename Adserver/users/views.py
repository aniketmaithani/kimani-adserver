# -*- coding: utf-8 -*-

# Third Party Stuff
from django.http import HttpResponse


def brand_view(request):
    if request.user.is_authenticated() and request.user.if_brand == True:
        return HttpResponse("You are Logged In")
