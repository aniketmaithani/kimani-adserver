# Third Party Stuff
from django.contrib.auth import authenticate
from django.views.generic import CreateView

# Kimani Adserver | Beta Stuff
from Adserver.users.models import CustomUser

from .forms import CouponForm
from .models import Coupon


class CouponCreate(CreateView):
    template_name = 'coupon_create.html'
    form_class = CouponForm
    success_url = 'thanks.html'


    def form_valid(self, form):
            form.instance.created_by = request.user
            return super(CouponCreate, self).form_valid(form)
