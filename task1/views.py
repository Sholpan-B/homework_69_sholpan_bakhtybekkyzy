import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_numbers(request, *args, **kwargs):
    data = json.loads(request.body)
    a = float(data.get('A'))
    b = float(data.get('B'))
    return a, b


def add(request):
    if request.method == 'POST':
        if request.body:
            try:
                a, b = get_numbers(request)
                answer = round(a + b)
                response = JsonResponse({'answer': answer})
                return response
            except ValueError:
                response = JsonResponse({'error': 'Input numbers only'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Only POST request are allowed'})
        response.status_code = 400
        return response


def subtract(request):
    if request.method == 'POST':
        if request.body:
            try:
                a, b = get_numbers(request)
                answer = round(a - b)
                response = JsonResponse({'answer': answer})
                return response
            except ValueError:
                response = JsonResponse({'error': 'Input numbers only'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Only POST request are allowed'})
        response.status_code = 400
        return response


def multiply(request):
    if request.method == 'POST':
        if request.body:
            try:
                a, b = get_numbers(request)
                answer = round(a * b)
                response = JsonResponse({'answer': answer})
                return response
            except ValueError:
                response = JsonResponse({'error': 'Input numbers only'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Only POST request are allowed'})
        response.status_code = 400
        return response


def divide(request):
    if request.method == 'POST':
        if request.body:
            try:
                a, b = get_numbers(request)
                if b == 0:
                    response = JsonResponse({'error': 'Division by zero!'})
                    response.status_code = 400
                    return response
                else:
                    answer = round((a / b), 2)
                    response = JsonResponse({'answer': answer})
                    return response
            except ValueError:
                response = JsonResponse({'error': 'Input numbers only'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Only POST request are allowed'})
        response.status_code = 400
        return response
