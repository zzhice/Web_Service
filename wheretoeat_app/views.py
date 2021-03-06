from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from apis.yelp import *
from apis.calendar import *
from apis.weather import *

yelp_key = ""
direction_key = ""
weather_key = ""

def start(request):

    return render(request, 'wheretoeat.html')


@csrf_exempt
@require_POST
def get_run(request):

    pre = request.POST.get('preference')
    location = request.POST.get('location')

    output_yelp = call_yelp(api_key=yelp_key, term=pre, location=location)
    # print(output_yelp)
    return JsonResponse(data=output_yelp)


@csrf_exempt
@require_POST
def get_history(request):

    result = call_calendar()

    return JsonResponse(data={'history_result': result})


@csrf_exempt
@require_POST
def get_weather(request):

    result = call_weather(weather_key)

    return JsonResponse(data={'weather_result': result})

@csrf_exempt
@require_POST
def get_info(request):
    end_location = request.POST.get('End_location')
    location = request.POST.get('location')

    pre = request.POST.get('preference')
    location = request.POST.get('location')

    output_yelp = call_yelp(api_key=yelp_key, term=pre, location=location)
    print(output_yelp)

    result = call_review(api_key=yelp_key, location=end_location, record=output_yelp)
    # result = call_directions(direction_key,location,end_location)

    return JsonResponse(data=result,safe=False)








