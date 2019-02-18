from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess




def index(request):
    # context = {}
    # context['hello'] = "Poppin' Party"
    # return HttpResponse('<h2>Hello World</h2>')
    return render(request, 'hello.html')


@csrf_exempt
@require_POST
def get_json(request):
    code = request.POST.get('code')
    output = run_code(code)
    return JsonResponse(data={'output': output})


def run_code(code):
    try:
        output = subprocess.check_output(['python','-c',code],\
                                         universal_newlines=True,\
                                         stderr=subprocess.STDOUT,\
                                         timeout=2)
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired as t:
        output = ''.join(["Time out",t.output])
    return output


# code = """import time \ntime.sleep(15)"""
# print(run_code(code))