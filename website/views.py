from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    #check to see login
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        #authenticate
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"There was an error!")
            return redirect('home')
    
    else:
        return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged Out....")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #authenticate and logged in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfuly signed up..")
            return redirect('home')
        
    else:
         return render(request,'register.html',{'form':SignUpForm() })
    
    return render(request,'register.html',{'form':SignUpForm() })