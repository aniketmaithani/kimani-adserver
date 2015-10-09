# Third Party Stuff
from django import forms

from .models import Coupon


class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = ['coupon_name', 'photo_of_the_coupon', 'coupon_code']
