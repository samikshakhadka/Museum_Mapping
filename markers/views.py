

from django.views import generic
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Marker

longitude = 85.3129501
latitude = 27.7120171

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Marker
    context_object_name = 'markers'
    queryset = Marker.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:10]
    print("--------------------------", queryset)
    template_name = 'index.html'

