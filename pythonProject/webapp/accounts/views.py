from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from .models import Patient

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        user=Patient()
        user.full_name = request.POST['full_name']
        user.user_name = request.POST['user_name']
        user.email = request.POST['email']
        user.phone_num = request.POST['phone_num']
        user.dob = request.POST['dob']
        user.house_name = request.POST['house_name']
        user.street = request.POST['street']
        user.city = request.POST['city']
        user.pincode= request.POST['pincode']
        user.password= request.POST['password1']
        user.gender = request.POST['gender']
        user.medicine=request.POST['med']


        # user=Patient.object.create_user(user_name=user_name,password=password1,email=email,full_name=full_name,phone_num=phone_num,dob=dob,house_name=house_name,street=street,city=city,pincode=pincode,gender=gender,medicine=medicine)
        user.save()
        print("user_created")
        return render(request, 'home.html')

    else:
        return render(request,'register.html')

