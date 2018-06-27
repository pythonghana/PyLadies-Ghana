from django.shortcuts import render


def events(request):
	context = {}
	template_name = 'events/events.html'
	return render(request, template_name, context)