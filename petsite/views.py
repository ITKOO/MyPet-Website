from django.shortcuts import render

from .models import Message


def menu_list(request):
    return render(request, 'menu/menu_list.html', {})


def message_list(request):
    messages = Message.objects.order_by('created_date')
    return render(request, 'message/message_list.html', {'messages': messages})
