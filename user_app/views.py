from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import View
from main_app .models import *
from django.http import HttpResponse



class users_profile(View):
    def get(self, request):
        my_user = Profile.objects.filter(is_active=True)
        return render(request, 'user_template/regster_user.html',{'form':my_user})

    def post(self, request):
        users = ProfileForm(request.POST,request.FILES)
        if users.is_valid():
            use = users.save(commit=False)
            flat = LoginDetails.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                user_type='USER'
            )
            use.user = flat
            use.save()

            return HttpResponse('''<script>alert(" Registration successfully.");window.location="restaurant_app/home_page"</script>''')

        return render(request, 'user_template/regster_user.html', {'fry':users})
