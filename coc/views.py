from django.shortcuts import render


def coc(request):
    context = {}
    template = 'coc/coc.html'
    return render(request, template, context)
