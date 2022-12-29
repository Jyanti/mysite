from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views import View
import json
from utils.file_handler import fetch_user_data, update_user_data
from django.utils.decorators import method_decorator
from user.models import User
# Create your views here.


# @require_http_methods(["POST"])
# @csrf_exempt
# def signup(request):
#     request_data = json.loads(request.body)
#     try:
        
#         # jsonFile = open("user_data.json","r")
#         # try:
#         #     data = json.load(jsonFile)
#         # except Exception as e:
#         #     data = []
#         # jsonFile.close()
        
#         data = fetch_user_data()
#         #[{"username": "asdadsa", "password": "3545", "name": "sanket"}, {"username": "hanky", "password": "5678", "name": "hanket"}]
        
#         data.append(request_data)
        
#         print(data)
        
#         jsonFile = open("user_data.json","w")
        
#         jsonFile.write(json.dumps(data))
        
#         jsonFile.close()
        
#         return JsonResponse({"msg": "user signed up"})
        
#     except Exception as e:
#         print(e)
#         return JsonResponse({"msg": "invalid parameters"}, status = 400)
    
    
    
# def index(request):
#     data = fetch_user_data()
#     return JsonResponse({"data":data})    
        
# @require_http_methods(["POST"])
# @csrf_exempt
# def login(request):
#     request_data = json.loads(request.body)
#     try:
#         data = fetch_user_data()
#         for users in data:
#          if users["username"] == request_data["username"]:
#             if users["password"] == request_data["password"]:
#                 return JsonResponse({"data":users},status = 200)
#             return JsonResponse({"msg": "username or password not present"}, status = 400)
             
#     except Exception as e:
#         print(e)
#         return JsonResponse({"msg": "username or password not present"}, status = 400)
    

# create an application user

#user/signup -- POST (API) {username, password, name} -- store data in json file
#user/login -- POSt (API) {username, password}
#user/ -- GET (API) {return all user}



@method_decorator(csrf_exempt, name = 'dispatch')
class SignUp(View):

    def post(self, request):
        request_data = json.loads(request.body)
        qs = User.objects.create(username = request_data["username"], password = request_data["password"], age = request_data["age"])
        print(qs)
        # data = fetch_user_data()
        # if not self.allow_user(data, request_data):
        #     return JsonResponse({"msg": "user already exits"})
        
        
        # #check to verify if username exists or not, If it exists simplyreturn 400 error and user already exits
        # #id : 1
        # #id : 2
        # request_data = self.add_id(data, request_data)
        # data.append(request_data) 
        # update_user_data(data)
        return JsonResponse({"msg": "user signed up"})
    
    def allow_user(self,data,request_data):
        username = data
        for i in data:
            if i["username"] == request_data["username"]:   
                return False
        
        return True
    
    # def add_id(self, data, request_data):
    #     request_data["id"] = len(data) + 1
    #     return request_data
    
    def get(self,request):
        qs = User.objects.all()
        print(qs)
        output = []
        for user in qs:
            single = {"id": user.id, "name": user.name, "username": user.username}
            output.append(single)
        return JsonResponse({"data": output})
       
class GetUserData(View):
    def get(self,request,user_id):
        qs_filter =  User.objects.filter(id = user_id)
        qs_get =  User.objects.get(id = user_id)
        print(qs_filter)
        #print(qs_get)
        if qs_filter.exists():
            resp = {"id": qs_filter[0].id, "name": qs_filter[0].name, "username": qs_filter[0].username}
            return JsonResponse({"data": resp})
            
        # for i in data:
        #     if i["id"] == user_id:
        #         return JsonResponse({"data":i})
        return JsonResponse({"msg":"user not found"})
                
       
       
    
       
# https://django_app.com/user/ -- POST , GET
# https://django_app.com/user/<int:user_id> -- PUT/PATCH , GET , DELETE 


# ecommerce

# categories --

# https://django_app.com/categories/ -- POST , GET

# https://django_app.com/categories/<int:category_id> -- PUT/PATCH , GET , DELETE 

# products
# https://django_app.com/category/<int:category_id>/products -- POST , GET
# https://django_app.com/category/<int:category_id>/products/<int:product_id>-- PUT/PATCH , GET , DELETE 