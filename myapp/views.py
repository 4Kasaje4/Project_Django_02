from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required 
from myapp.forms import RegisterForm , UserProfileForm ,ExtendedProlfileForm , PostForm , PasswordChangingForm
from django.contrib.auth.models import User
from .models import postdata 
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
@login_required
def password_success(request):
    messages.success(request, "Change password successfully")
    return redirect('/home' , {'messages' : messages})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

@login_required
def index(request):
    return render(request,'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.success( request,"Something wrong please try again")
            return redirect('/login' , {'message' : messages})    
    else:
        return render(request,'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def home(request):
    data = postdata.objects.all()
    num_u = User.objects.all().values()
    arraydata = []
    n= 0
    for i in num_u:
        arraydata.append(i)
    for i in arraydata:
        n = n + 1
    print(n)
    return render(request,'home.html' , {'data': data , 'n' : n} )

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register Successfully")
            return redirect('/' , {'messages' : messages})

    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html' , {'form' : form} ,)


@login_required
def profile(request):
    
    if request.method == "POST":

        is_new_profile = False

        form = UserProfileForm(request.POST , instance=request.user)
        
        try:
            extended_from = ExtendedProlfileForm(request.POST , instance=request.user.member)
        except:
            extended_from = ExtendedProlfileForm(request.POST)
            is_new_profile = True

        if form.is_valid() and extended_from.is_valid():
            form.save()
            if is_new_profile :
                user = extended_from.save(commit=False)
                user.user = request.user
                user.save()
            else:
                extended_from.save()
            messages.success(request,'Edit profile Successfully')
            return redirect('/home' , {'messages', messages})
    else:
        form = UserProfileForm(instance=request.user)
        try:
            extended_from = ExtendedProlfileForm(instance=request.user.member)
        except:
            extended_from = ExtendedProlfileForm()
    data = postdata.objects.all()
    context = {'form' : form , 'extended_form' : extended_from , 'data' : data}
    return render(request, 'profile.html', context ) 

@login_required
def post(request):
    if request.method == "POST":

        
        extended_from = PostForm(request.POST)

        if  extended_from.is_valid():
            user_post = extended_from.save(commit=False)
            user_post.user = request.user
            user_post.save()
            messages.success(request,'Post Successfully')
            return redirect('/home' , {'messages', messages })
    else:
        extended_from = PostForm()
    context = {'extended_form' : extended_from }
    return render(request, 'post.html', context )

@login_required
def edit(request ,user_id):
    data = postdata.objects.get(id = user_id)
    if request.method == "POST":
        user_description = postdata.objects.get(id = user_id)
        new_description = request.POST['description']
        user_description.description = new_description
        user_description.save()
        messages.success(request,"Edit post successfully")
        return redirect('/home',{'messages': messages})
    context = {'data' : data}
    return render(request, 'edit.html', context )

@login_required
def delete(request, id):
    data = postdata.objects.get(id= id)
    data.delete()
    messages.success(request,"Delete successfully")
    return redirect('/home',{'messages':messages})


def delete_account(request):
    account = User.objects.get(id = request.user.id)
    account.delete()
    messages.success(request,"Delete account successfully")
    return redirect('/',{'messages' : messages})

def about(request):
    return render(request, 'about.html')