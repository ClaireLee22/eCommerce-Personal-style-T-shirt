from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Personal style T-shirt",
        "content": "Welcome!!",
    }
   
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About Page!",
        "content": "Welcome to the about page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us!",
        "content": "Welcome to the conatct page",
        "form": contact_form,
        "brand": "new brand name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json() # already json
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type="application/json")
    return render(request, "contact/view.html", context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print(request.user.is_authenticated)
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            # context["form"] = LoginForm()
            return redirect("/")

        else:
            # Return an "invalid login" error message
            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)

def home_page_old(request):
    return HttpResponse("<h1>Hello world</h1>")