from django.http import QueryDict

def put_middleware(get_responese):
    def middleware(request):
        if request.method == 'PUT':
            setattr(request, 'PUT', QueryDict(request.body))
        response = get_responese(request)
        return response
    return middleware