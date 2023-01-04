from django.shortcuts import render
from assignment2.models import Users
from django.views import View
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(csrf_exempt, name = 'dispatch')
class UserView(View):

    def get(self,request):
            qs = Users.objects.all()
            print(qs)
            output = []
            for user in qs:
                single = {"id": user.id, "name": user.name, "username": user.username}
                output.append(single)
            return JsonResponse({"data": output})

    def post(self, request):
            request_data = json.loads(request.body)
            qs = Users.objects.create(username = request_data["username"], password = request_data["password"], age = request_data["age"])
            print(qs)
            return JsonResponse({"data": "user created"})
    
    #Create a user module. Post and get 
#{GET, UPDATE,DELETE} filter(id = user_id).update(name = "ggg")
                  # .filter{id = user_id}.delete()
                  
    def delete(self,request):
        request_data = json.loads(request.body)
        
        existingUser = Users.objects.first(username = request_data["username"]);
        
        #find that user in table
        # if (user)
            # then delete that by that Id
        
        qs = Users.objects.filter(id = existingUser.id).delete()
        print(qs)
        
    def update(self, request):
        request_data = json.loads(request.body)
        existingUser = Users.objects.first(username = request_data["username"]);
        qs = Users.objects.filter(id = existingUser.id).update()
        print(qs)
        
        