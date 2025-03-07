from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import admin_only
from merchant.models import Products, Tax


# # Create your views here.
# def signin(request):
#     return HttpResponse("<h1>App Is Working</h1>")

@admin_only
def index(request):
    products = Products.objects.all()

    context = {
        "products":products
    }
    return render(request,"index.html",context)

def admin_index(request):
    return render(request,"admin_index.html")

def merchant_index(request):
    return render(request,"merchant/merchant_index.html")


def service_index(request):
    return render(request,"service/index.html")


def signin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username = uname, password = pswd)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request,"Username or password incorrect")
            return redirect("signin")
        print(uname, pswd,"-------------------------------------------")
    return render(request, 'login.html')


def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registered Success....")
            return redirect("signin")
        else:
            messages.error(request,form.errors)
            return redirect("signup")
        
    context = {
        "form":form
    }
    return render(request,'register.html',context)

def signout(request):
    logout(request)
    return redirect(signin)



def tax_mgt(request):
    taxs = Tax.objects.all()
    if request.method == "POST":
        tax_name = request.POST.get("tax_name")
        tax_value = request.POST.get("tax_value")

        tax = Tax.objects.create(tax_name  = tax_name, tax_value = tax_value )
        tax.save()

        messages.success(request,"Tax Value Saved")
        return redirect("tax_mgt")


    context = {
        "taxs":taxs
    }
    return render(request,"admin/tax.html",context)


def edit_tax(request, pk):
    tax = get_object_or_404(Tax, id = pk)

    if request.method == "POST":
        tax_name = request.POST.get("tax_name")
        tax_value = request.POST.get("tax_value")

        tax.tax_name = tax_name
        tax.tax_value = tax_value

        tax.save()
        messages.success(request,"Tax, Value Updated.....")
        return redirect(tax_mgt)

    context = {
        "tax":tax
    }
    return render(request,"admin/update_tax.html",context)


def delete_tax(request, pk):
    Tax.objects.get(id = pk).delete()
    messages.success(request,"Tax, Value Updated.....")
    return redirect(tax_mgt)


from .models import CustomUser, Chat_Messages

def chat_user_list(request):
    users = CustomUser.objects.all()
    context = {
        "users":users
    }
    return render(request,"chat_user_list.html",context)


def chat_view(request, user_id):
    """ Load the chat interface between two users. """
    other_user = get_object_or_404(CustomUser, id=user_id)

    if request.user.id == other_user.id:
        import django.contrib.messages
        django.contrib.messages.info(request,"You Cannot sent Self message ")
        return redirect("index")

    # Fetch previous messages between two users
    messages = Chat_Messages.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("created_at")

    return render(request, "chat_with_merchant.html", {"messages": messages, "other_user": other_user})



def chat_list_merchant(request):
    users = CustomUser.objects.all()
    context = {
        "users":users
    }
    return render(request,"merchant/chat_user_list.html",context)

def chat_with_user(request, user_id):
    
    """ Load the chat interface between two users. """
    other_user = get_object_or_404(CustomUser, id=user_id)

    if request.user.id == other_user.id:
        import django.contrib.messages
        django.contrib.messages.info(request,"You Cannot sent Self message ")
        return redirect("index")

    # Fetch previous messages between two users
    messages = Chat_Messages.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("created_at")

    return render(request, "chat_with_user.html", {"messages": messages, "other_user": other_user})


def user_profile_update(request):
    user = request.user

    form = UserUpdateForm(instance = user)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            messages.success(request,"User Update Success....")
            return redirect("user_profile_update")
        else:
            messages.error(request,form.errors)
            return redirect("user_profile_update")

    context = {
        "form":form
    }
    return render(request,"profile_page.html",context)


def user(request):
    form1 = UserAddForm()
    
    users = CustomUser.objects.filter(role = "user")
    if request.method == "POST":
        form1 = UserAddForm(request.POST)
       
        if form1.is_valid():
            user = form1.save()
            user.role = "user"
            user.save()
           
            messages.success(request,"User Registration Successful")
            return redirect("user")
        else:
            messages.error(request,f"Something went Wrong!!! Try To use password Includes (UPPERCASE, Numbers, Sepecial Characters and Minimum Legth 8  Characters) or User or email id Already Exists <br> {form1.errors} <br>")
            return redirect("user")

    context = { "form1":form1,"users":users}   
    return render(request,"admin/users_admin.html",context)

def user_update(request,id):
    user = CustomUser.objects.get(id=id)
   
    form1 = UserUpdateForm(instance=user)
   
    if request.method == "POST":
        form1 = UserUpdateForm(request.POST, instance=user)
       
        if form1.is_valid():
            form1.save()
            
            messages.success(request,"user Updated Successfully")
            return redirect("user")
        else:
            messages.error(request,"Something went Wrong!!!")
            return redirect("user")
    context = {"form1":form1, "volunteer":user}
    return render(request,"admin/users_update.html",context)

def user_delete(request,id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    messages.success(request,"User Deleted Successfully")
    return redirect("user")




def service_provider(request):
    form1 = UserAddForm()
    
    service_provider = CustomUser.objects.filter(role = "service_provider")
    if request.method == "POST":
        form1 = UserAddForm(request.POST)
       
        if form1.is_valid():
            user = form1.save()
            user.role = "service_provider"
            user.save()
           
            messages.success(request,"service_provider Registration Successful")
            return redirect("service_provider")
        else:
            messages.error(request,f"Something went Wrong!!! Try To use password Includes (UPPERCASE, Numbers, Sepecial Characters and Minimum Legth 8  Characters) or User or email id Already Exists <br> {form1.errors} <br>")
            return redirect("service_provider")

    context = { "form":form1,"service_provider":service_provider}   
    return render(request,"admin/service_provider.html",context)

def service_provider_update(request,id):
    service_provider = CustomUser.objects.get(id=id)
   
    form1 = UserUpdateForm(instance=service_provider)
   
    if request.method == "POST":
        form1 = UserUpdateForm(request.POST, instance=service_provider)
       
        if form1.is_valid():
            form1.save()
            
            messages.success(request,"service_provider Updated Successfully")
            return redirect("service_provider")
        else:
            messages.error(request,"Something went Wrong!!!")
            return redirect("service_provider")
    context = {"form1":form1, "volunteer":user}
    return render(request,"admin/edit_service_provider.html",context)

def delete_service_provider(request,id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    messages.success(request,"Service provider Deleted Successfully")
    return redirect("service_provider")




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Service_booking
from .forms import ServiceForm, ServiceBookingForm


def service_user(request):
    services = Service.objects.all()
    form  = ServiceBookingForm()
    return render(request,"services.html",{"services":services,"form":form})

@login_required(login_url="signin")
def myservice_booking(request):
    bookings = Service_booking.objects.filter(booked_by = request.user)
    return render(request,"myservice_booking.html",{"bookings":bookings})

@login_required(login_url="signin")
def add_service(request):
    services = Service.objects.filter(servicer = request.user)
    if request.method == "POST":
        
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.servicer = request.user
            service.save()
            return redirect('add_service')  # Redirect to service list page
    else:
        form = ServiceForm()
    return render(request, 'service/add_service.html', {'form': form,"services":services})

@login_required(login_url="signin")
def update_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, servicer=request.user)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('add_service')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service/update_service.html', {'form': form})

@login_required(login_url="signin")
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, servicer=request.user)
    service.delete()
    return redirect('add_service')

@login_required(login_url="signin")
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = ServiceBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.booked_by = request.user
            booking.service = service
            booking.save()
            return redirect('service_user')  # Redirect to user's bookings
    else:
        form = ServiceBookingForm()
    return render(request, 'services/book_service.html', {'form': form, 'service': service})


@login_required(login_url="signin")
def booking_list(request):
    bookings = Service_booking.objects.filter(service__servicer=request.user)
    return render(request, 'service/booking.html', {'bookings': bookings})

@login_required(login_url="signin")
def approve_booking(request, booking_id):
    booking = get_object_or_404(Service_booking, id=booking_id, service__servicer=request.user)
    booking.approve = True
    booking.save()
    messages.success(request, "Booking approved successfully.")
    return redirect('booking_list')

@login_required(login_url="signin")
def reject_booking(request, booking_id):
    booking = get_object_or_404(Service_booking, id=booking_id, service__servicer=request.user)
    booking.approve = False
    booking.save()
    messages.success(request, "Booking rejected successfully.")
    return redirect('booking_list')