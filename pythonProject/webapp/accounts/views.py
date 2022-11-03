from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
# Create your views here.



def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        phone_num = request.POST['phone_num']
        dob = request.POST['dob']
        house_name = request.POST['house_name']
        street = request.POST['street']
        city = request.POST['city']
        pincode= request.POST['pincode']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        gender = request.POST['gender']
        medicine=request.POST['medicine']


        user=User.object.create_user(user_name=user_name,password=password1,email=email,full_name=full_name,phone_num=phone_num,dob=dob,house_name=house_name,street=street,city=city,pincode=pincode,gender=gender,medicine=medicine)
        user.save()
        print("user_created")
        return render(request, 'home.html')

    else:
        return render(request,'register.html')
