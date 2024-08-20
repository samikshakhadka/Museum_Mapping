from django.views import generic
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from .models import Marker

class Home(generic.ListView):
    model = Marker
    context_object_name = 'markers'
    template_name = 'index.html'

    def get_queryset(self):
        return Marker.objects.all()

def get_markers(request):
    longitude = request.GET.get('longitude')
    latitude = request.GET.get('latitude')

    if longitude and latitude:
        user_location = Point(float(longitude), float(latitude), srid=4326)
        markers = Marker.objects.annotate(distance=Distance('location', user_location)).order_by('distance')
        
    else:
        markers = Marker.objects.all()

    # Prepare all markers data
    all_markers_data = [
        {
            
            "name": marker.name,
            "lat": marker.location.y,
            "lng": marker.location.x,
            "distance": getattr(marker, 'distance', None) and marker.distance.m
        }
        for marker in markers
    ]

    response_data = {
        "all_markers": all_markers_data,
    }
    return JsonResponse(response_data)
