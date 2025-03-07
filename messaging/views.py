from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from .forms import MessageForm

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)