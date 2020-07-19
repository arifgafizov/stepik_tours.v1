from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError

from tours.data import departures, tours


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html'
        )


class DepartureView(View):
    def get(self, request, departure):
        data = {"departure": departures[departure]}
        return render(request, "tours/departure.html", context=data)


class TourView(View):
    def get(self, request, id):
        data = tours[id]
        return render(request, 'tours/tour.html', context=data)


def custom_handler404(request, exception):
    return HttpResponseNotFound("<h1>page not found</h1>")


def custom_handler500(request):
    return HttpResponseServerError("<h1>server error</h1>")
