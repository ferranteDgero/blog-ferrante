from django.urls import path
from .views import MessageListView, MessageCreateView

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('send/', MessageCreateView.as_view(), name='message_send'),
]