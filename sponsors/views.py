from django.shortcuts import render


def sponsors(request):
    context = {}
    template = 'sponsors/sponsors.html'
    return render(request, template, context)
