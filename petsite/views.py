from django.shortcuts import render

from .models import Message, Gallery, Snack


def introduce(request):
    return render(request, 'introduce/introduce.html', {})


def menu_list(request):
    return render(request, 'menu/menu_list.html', {})


def message_list(request):
    messages = Message.objects.order_by('created_date')
    return render(request, 'message/message_list.html', {'messages': messages})


def gallery(request):
    gallery = Gallery.objects.order_by('created_date')
    return render(request, 'gallery/gallery.html', {'gallery': gallery})


def snack_list(request):
    snacks = Snack.objects.order_by('created_date')
    return render(request, 'snack/snack_list.html', {'snacks': snacks})
