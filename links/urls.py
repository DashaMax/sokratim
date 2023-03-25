from django.urls import path

from links.views import LinkDeleteView, LinksView

urlpatterns = [
    path('user/<slug>/', LinksView.as_view(), name='links'),
    path('user/<slug>/delete-link/<int:pk>/', LinkDeleteView.as_view(), name='link_delete'),
]