from django.shortcuts import render
from django.http import HttpResponse


def test_text(request):
    with open('./media/test_text.txt', 'rb') as file:
        response = HttpResponse(file.read())
        response['Content-Type'] = 'text'
        response['Content-Disposition'] = 'attachment; filename="test_text.txt"'
    return response


def download_file(request, filename):
    with open('./media/' + filename, 'rb') as file:
        response = HttpResponse(file.read())
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response