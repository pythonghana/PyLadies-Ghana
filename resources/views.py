from django.shortcuts import render


def resources(request):
    context = {}
    template = 'resources/resources.html'
    return render(request, template, context)


