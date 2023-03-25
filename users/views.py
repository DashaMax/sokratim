from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserEnterForm, UserRegistrationForm, UserUpdateForm
from users.models import User


class MainPageView(TemplateView):
    template_name = 'users/index.html'
    extra_context = {'title': 'Сокра.тим'}


class UserEnterView(LoginView):
    template_name = 'users/enter.html'
    form_class = UserEnterForm
    extra_context = {'title': 'Сокра.тим - вход'}

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.request.user.slug, ))

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super(UserEnterView, self).get(request, *args, **kwargs)


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_message = 'Вы успешно зарегистрировались!'
    extra_context = {'title': 'Сокра.тим - регистрация'}
    success_url = reverse_lazy('enter')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super(UserRegistrationView, self).get(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/profile.html'
    model = User
    form_class = UserUpdateForm
    success_message = 'Профиль успешно обновлён!'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Сокра.тим - личный кабинет'
        context['username'] = User.objects.get(slug=self.kwargs['slug'])
        context['email'] = User.objects.get(slug=self.kwargs['slug']).email
        return context

    def get(self, request, *args, **kwargs):
        if kwargs['slug'] != request.user.slug:
            return redirect('main')
        return super(UserProfileView, self).get(request, *args, **kwargs)


