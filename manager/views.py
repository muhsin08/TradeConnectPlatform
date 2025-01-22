from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from main_app .models import *
from worker_app.models import *
# Create your views here.
class Verify(View):
    def get(self,request):
        user_status=LoginDetails.objects.filter(user_type='WORKER',status='pending')
        cert_status=WorkerProfile.objects.all()
        return render(request,'manager_template/verify_worker.html',{'user_status':user_status,'cert':cert_status})
    def post(self,request,id):
        user_data=get_object_or_404(LoginDetails,id=id)
        new_status=request.POST.get('status')
        other=['verified','rejected']
        if new_status not in other:
            messages.error(request,"status not changed")
            return redirect('verify')
        user_data.status=new_status
        user_data.save()
        messages.success(request,f"{user_data.username} profile {user_data.status} sucessfully")
        return redirect('verify')
