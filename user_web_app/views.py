from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required #73 django_text
#from django.contrib.auth.forms import UserCreationForm # since now no use after calling  UserRegisterForm
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# Create your views here.
def register(request):
    if request.method=='POST':

        #form_1 = UserCreationForm(request.POST) #in place of this we call  new inherited userRegister form
        form_1 = UserRegisterForm(request.POST)
        if form_1.is_valid():
            form_1.save()
            username = form_1.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}! You can now login")
            return redirect('login')#change from blog-home to login
    else:
        form_1 = UserRegisterForm() # same as above replacement
    return render(request,'user_web_app/register.html',{'form':form_1})
@login_required #73
def profile(request): #71(django test)
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)#-->109
        profile_form=ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():#-->108
            user_form.save()
            profile_form.save()
           # username = form_1.cleaned_data.get('username')
            messages.success(request,f"Your Account Has Been updated ")
            return redirect('profile')#-->110
    else:
        user_form = UserUpdateForm( instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile) #-->107
    context={
        'u_form':user_form,
        'p_form':profile_form
    }
    return render(request,'user_web_app/profile.html',context)


