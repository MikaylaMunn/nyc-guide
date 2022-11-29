from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    def get (self, request, borough, activity):
        # similar to the above class, except I needed borough, activity, and venues for the link I would create in activity.html
        return render(
            request = request,
            template_name='activity.html',
            context ={
                'borough': borough,
                'activity': activity,
                'venues': boroughs[borough][activity].keys()
            }
        )


class VenueView(View):
    def get(self, request, borough, activity, venue):
        return render (
            request = request,
            template_name = 'venue.html',
            # what do I want displayed on the html page
            context = {
                'borough': borough,
                'activity': activity,
                # accessed the dicitonary until I got to the img_link and description section
                'venue': venue, 'img': boroughs[borough][activity][venue]['img_link'], 'description': boroughs[borough][activity][venue]['description']
            }
        )
