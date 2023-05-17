from django.shortcuts import render

from .models import Message


# Create your views here.

def menu_list(request):
    messages = Message.objects.order_by('created_date')
    return render(request, 'menu/menu_list.html', {'messages': messages})
