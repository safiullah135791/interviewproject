from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from .models import Datas
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def addData(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = request.POST['input2']
        input3 = request.POST['input3']
        input4 = request.POST['input4']
        input5 = request.POST['input5']
        input6 = request.POST['input6']
        input7 = request.POST['input7']
        input8 = request.POST['input8']
        input9 = request.POST['input9']
        input10 = request.POST['input10']
        
        obj = Datas()
        obj.morning10 = input1
        obj.afternoon2 = input2
        obj.evening6 = input3
        obj.night10 = input4
        obj.firsttotal = input5
        obj.firstrupess10 = input6
        obj.rupess2 = input7
        obj.rupess6 = input8
        obj.lastrupess10 = input9
        obj.lasttotal = input10
        obj.save()

        mydata = Datas.objects.all()
        return redirect('home')
    return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname =  request.POST.get('username')
        email =  request.POST.get('email')
        pass1 =  request.POST.get('password1')
        pass2 =  request.POST.get('password2')

        # regExp ='/^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.([a-zA-Z])?$/'

        if pass1 != pass2:
            messages.error(request,'Password not same')
        elif get_user_model().objects.filter(username = uname).exists():
             messages.error(request,'Username already exists')
             return redirect('signup')
        elif get_user_model().objects.filter(email = email).exists():
            messages.error(request,'email already exists')
            return redirect('signup')
        elif get_user_model().objects.filter(password = pass1).exists():
            messages.error(request,'password already exists')
            return redirect('signup')
        elif (not uname):
            messages.error(request,'username is required')
        elif len(uname) < 4:
            messages.error(request,'First name not less than 4 char long')
        elif len(uname) > 20:
            messages.error(request,'First name not more than 20 char long')
        elif (not email) :
            messages.error(request,'email is required')
      #  elif (regExp != email):
      #      messages.error(request,'Enetr correct format of email')
        elif len(pass1) < 4:
            messages.error(request,'First name not more than 20 char long')
        elif len(pass1) > 16:
            messages.error(request,'First name not more than 20 char long')
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            messages.success(request,'Your account has been successfully created')
            return redirect('login')

    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        pass1 =  request.POST.get('pass')

        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            name = user.username
            messages.success(request,'You successfully logedin %s' %(name),)
            return redirect('home')
        elif (not username):
            messages.error(request,'username is required')
        elif (not pass1):
            messages.error(request,'password is required')
        else:
            messages.error(request,'Username and Password is incorrect')
            return redirect('login')
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    messages.success(request,'You successfully logedout')
    return redirect('login')
