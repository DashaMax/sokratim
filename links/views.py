from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from links.forms import LinkForm
from links.models import Link


class LinksView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'links/links.html'
    form_class = LinkForm
    success_message = 'Ссылка успешно добавлена!'

    def get_context_data(self, **kwargs):
        context = super(LinksView, self).get_context_data(**kwargs)
        context['title'] = 'Сокра.тим - ссылки'
        context['links'] = Link.objects.filter(username=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('links', args=(self.request.user.slug, ))

    def post(self, request, *args, **kwargs):
        link = request.POST.copy()
        short_link = request.user.slug + '/' + link['short_link']
        link['username'] = request.user
        link['short_link'] = short_link
        request.POST = link
        return super(LinksView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs['slug'] != request.user.slug:
            return redirect('main')
        return super(LinksView, self).get(request, *args, **kwargs)


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = Link
    template_name = 'links/links.html'

    def get_success_url(self):
        return reverse_lazy('links', args=(self.request.user.slug, ))

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
