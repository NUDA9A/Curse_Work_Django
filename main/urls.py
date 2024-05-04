from django.urls import path

from main.apps import MainConfig
from main.views import HomePageView, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('mailings/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
]
