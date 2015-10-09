from django.views.generic import CreateView, DetailView, ListView

from .forms import CouponForm
from .models import Coupon
from Adserver.users.models import CustomUser


class CouponCreate(CreateView):

    template_name = 'coupon_create.html'
    form_class = CouponForm
    success_url = 'thanks.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CouponCreate, self).form_valid(form)


