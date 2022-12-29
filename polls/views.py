from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Create your views here.

from django.http import HttpResponse,  JsonResponse


@csrf_exempt
def index(request):
    print(request.method)
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(["GET", "POST"])
@csrf_exempt
def new_sss(request):
   if request.method != ["GET"]:
       return JsonResponse({"msg":"Failed"}, status = 405)
   return JsonResponse({"msg": "SSS function executed"}, status = 200)

   #return HttpResponse("SSS function excuited.")
   
@require_http_methods(["POST"])
@csrf_exempt
def addition_two_number(request):
    data = json.loads(request.body)
    print(data)
    print(type(data))
    final_sum = data["num1"] + data["num2"]
    return JsonResponse({"msg": final_sum}, status = 200)

@require_http_methods(["GET"])
@csrf_exempt
def addition_two_number_url(request, num1, num2):
    final_sum = 0
