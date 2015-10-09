# Third Party Stuff
from django.contrib.auth import authenticate
from django.views.generic import CreateView, DetailView, ListView

# Kimani Adserver | Beta Stuff
from Adserver.users.models import CustomUser

from .forms import CouponForm
from .models import Coupon


class CouponCreate(CreateView):
    template_name = 'coupon_create.html'
    form_class = CouponForm
    success_url = 'thanks.html'

    @login_required
    def form_valid(self, form):
        if self.request.user.if_brand:
            form.instance.created_by = self.request.user
            return super(CouponCreate, self).form_valid(form)
