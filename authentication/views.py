from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#updates from chris
from .forms import UserSignUpForm



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, "authentication/index.html")
    else:
        messages.success(request, "you must be logged in to access the home page")    
        return redirect ('signin')

def signup(request):
    #chris updates for signing up
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully')
            return redirect ('signin')
        messages.success(request, "Check form and provide the needed information")
        return render(request, "authentication/signup.html", {'form': form}) 
    form = UserSignUpForm
    return render(request, "authentication/signup.html", {'form': form}) 




    # if request.method == "POST":
    #     # username = request.POST.get('username')
    #     username = request.POST['username']
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     pass1 = request.POST['pass1']
    #     pass1 = request.POST['pass2']

    #     myuser = User.objects.create_user(username, email, pass1)
    #     myuser.first_name = fname
    #     myuser.last_name = lname


    #     myuser.save()

    #     messages.success(request, "Your Account has been successfully created.")

    #     return redirect('signin')


    # return render(request, "authentication/signup.html")
    
    
    
    
    

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name.capitalize()
            return render(request, "authentication/index.html",{'fname':fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('signin')