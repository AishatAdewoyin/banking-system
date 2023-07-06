# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib.auth.models import User

# import json

# # Create your views here.
# from django.http import JsonResponse
# import json

# class PersonalFullnameValidationView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         fullname = data['fname']

#         if not str(fullname).isalpha():
#             return JsonResponse({'fullname_error': 'Full names should only contain alphabets'})
#         return JsonResponse({'fullname_valid': True})



from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

import json
from django.views.generic import View

class PersonalFullnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        fullname = data['fname']

        if not str(fullname).isalpha():
            return JsonResponse({'fullname_error': 'Full names should only contain alphabets'})
        return JsonResponse({'fullname_valid': True})






        # Continue with further processing or return a response


        

    
# class businessRegView(view):
#     def get(self, request):
#         return render(request, 'authentication/customers-reg/business-reg.html')
    
# class investorRegView(view):
#     def get(self, request):
#         return render(request, 'authentication/customers-reg/invest-reg.html')
