from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
# def dashboard(request):
#     return render(request, 'dashboard/index.html')

def volunteers(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        number = request.POST['number']
        age = request.POST["age"]
        department = request.POST['department']
        experience = request.POST["experience"]
        bootcamp = request.POST["bootcamp"]
        membership = request.POST['membership']
        publicity = request.POST['publicity']
        expectation = request.POST['expectation']
        checkbox = request.POST["checkbox"]
        print("got here")
        print(department, last_name, first_name, checkbox)

        if Volunteer.objects.filter(last_name=last_name).exists():
            if Volunteer.objects.filter(last_name=last_name).exists():
                print('Records already exist')
                messages.error(request, 'Records for that name already exist!')
                return render(request, 'volunteers.html')

        elif Volunteer.objects.filter(email=email).exists():
            print('email Taken')
            messages.error(request, 'Email Address Already Exist!')
            return render(request, 'volunteers.html')

        else:
            print(department, last_name, first_name, bootcamp)
            volunteer = Volunteer.objects.create(first_name=first_name, 
                last_name=last_name, 
                email=email, 
                whatsapp_number=number, 
                age=age, 
                department=department, 
                will_be_available_for_bootcamp = bootcamp,
                is_a_member_of_LTA=membership, 
                months_of_experience=experience,
                how_did_you_hear_of_us=publicity, 
                expectations_for_SOTS=expectation)
            volunteer.save();
            print(f"Saved\n{volunteer}")
            print('Form Submitted')
            messages.success(request, 'Form Submitted!. Kindly check your mail for more info')
            return redirect('volunteers')

    return render(request, "volunteers.html")


def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        number = request.POST['number']
        membership = request.POST['membership']
        publicity = request.POST['publicity']
        expectation = request.POST['expectation']

        if Registration.objects.filter(last_name=last_name).exists():
            if Registration.objects.filter(first_name=first_name).exists():
                print('Records already exist')
                messages.error(request, 'Records for that name already exist!')
                return render(request, 'signup.html')
        
        elif Registration.objects.filter(email=email).exists():
            print('email Taken')
            messages.error(request, 'Email Address Already Exist!')
            return render(request, 'signup.html')
                          
        else:
            user = Registration.objects.create(first_name=first_name, last_name=last_name, email=email, whatsapp_number=number, is_a_member_of_LTA=membership, how_did_you_hear_of_us=publicity, expectations_for_SOTS=expectation)
            #user.is_active = False
            user.save();
            print('Form Submit')
            messages.success(request, 'Form Submitted!. Kindly check your mail for more info')
            return redirect('register')
                
    return render(request, 'signup.html')
