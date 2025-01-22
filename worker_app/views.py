from django.shortcuts import render, redirect
from .forms import WorkerProfileForm
from .models import WorkerProfile, LoginDetails
from django.views import View
from main_app .models import *
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404



class Workers_profile(View):
    def get(self, request):
        work = WorkerProfile.objects.filter(is_active=True)
        return render(request, 'workers_template/register_work.html',{'form':work})

    def post(self, request):
        my_work = WorkerProfileForm(request.POST,request.FILES)
        if my_work.is_valid():
            working = my_work.save(commit=False)
            flat = LoginDetails.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                user_type='WORKER'
            )
            working.user = flat
            working.save()

            return HttpResponse('''<script>alert(" Registration successfully.");window.location="restaurant_app/home_page"</script>''')

        return render(request, 'workers_template/register_work.html', {'fry':my_work})





# class ViewProfile(View):
#     def get(self, request, id):
#         items = get_object_or_404(WorkerProfile, pk=id)
#         # Assuming `LoginDetails` has a `user` field that is a foreign key to `WorkerProfile`
#         my_user = LoginDetails.objects.filter(user=items)
#         return render(request, 'workers_template/manage_skills.html', {'user': items, 'my_user': my_user})

class ViewProfile(View):
    def get(self,request):
        user=WorkerProfile.objects.all()
        my_user=LoginDetails.objects.all()
        return render(request,'workers_template/manage_skills.html',{'user':user ,'my_user':my_user})





