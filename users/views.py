from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.services import send_code_email
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # self.object = form.save()
        # send_code_email(id=self.object.id, recipient_list=[self.object.email])
        obj = form.save()
        send_code_email(obj)
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verification_user(request):
    pk = request['pk']
    user = User.objects.get(pk=pk)
    user.is_verification = True
