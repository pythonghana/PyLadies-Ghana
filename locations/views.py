from django.shortcuts import render


def locations(request):
    context = {}
    template = 'locations/locations.html'
    return render(request, template, context)

