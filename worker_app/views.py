from multiprocessing.pool import worker
from django.contrib import messages

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






class ViewProfile(View):
    def get(self,request):
        worker_id=request.session['login_id']
        print("asdasdadas",worker_id)
        data=WorkerProfile.objects.filter(user=worker_id)

        return render(request,'workers_template/manage_skills.html',{'user':data})
class certificate_edit(View):
    def get(self, request, id):
        edit_certificate = get_object_or_404(WorkerProfile, pk=id)
        return render(request, 'workers_template/update_skill.html', {'data': edit_certificate})

    def post(self, request, id):
        edited_certificates = get_object_or_404(WorkerProfile, pk=id)
        edit_form = WorkerProfileForm(request.POST, request.FILES, instance=edited_certificates)
        if edit_form.is_valid():
            datas = edit_form.save(commit=False)
            datas.connect = LoginDetails.objects.get(id=request.session['login_id'])
            datas.save()
            messages.success(request, 'document edited')
            return redirect('view_profile')
        return render(request,"workers_template/update_skill.html",{'edited':edited_certificates})




