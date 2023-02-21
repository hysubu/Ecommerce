from django.shortcuts import render,redirect
from cryptography.fernet import Fernet
from User .models import *
from django.contrib import messages 

# Create your views here.


# User Regestration View section >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

def regestration(request):
    try :
        if request.method == "POST" :
            username = request.POST["username"]
            contact = request.POST["contact"]
            email = request.POST["email"]
            p_photo = request.FILES['profile']
            password = request.POST["password"]
            confirm_pass = request.POST["confirm-password"]
            passwordkey = Fernet.generate_key()
            # print("password_key ::--",passwordkey)
            fernet = Fernet(passwordkey)
            # print("fernate:--",fernet)
            encpassword = fernet.encrypt(password.encode())
            # print("encrypt_pass::==", encpassword) 
            # decpassword = fernet.decrypt(encpassword).decode()
            # print(encpassword)    
            # print(passwordkey)
            # print(decpassword)

            if len(password) == 8 :
                    if password == confirm_pass :
                        user = User(username = username,password =encpassword.decode('utf-8'),password_key = passwordkey.decode('utf-8'),email = email,profile_photo = p_photo,contact_number = contact )
                        user.save()
                        messages.success(request,'Registration Successfully .. !!')
                    else :
                        messages.error(request,'Password Does not match..!')
        return render(request,'Regestration.html')
    except Exception as e :
        print(e)


def login(request):
    try:
        if request.method == "POST":
            l_email = request.POST["email"]
            l_pass = request.POST['password']
            user_data  = User.objects.get(email=l_email)
            print("userpassowrd::--",user_data.password)
            print("userpassword_key::--",user_data.password_key)
            if user_data:
            # password_key = user_data.password_key
            # print(password_key)
                fernet = Fernet(user_data.password_key)
                print("fernate::-",fernet)
            # encpassword = fernet.encrypt(l_pass.encode())
                decpassword = fernet.decrypt(user_data.password).decode()
                print("decordpassword:--",decpassword)
                # cat = views.product_catagory(request)
         
                if l_pass == decpassword :
                    session_id = request.session["username"] = user_data.username
                    session_id = request.session["id"] = user_data.id

                    print("session_id",session_id)
                    # subject = " Welcome to Our E-commerce Website "
                    # message = f'Hi {user_data.first_name} we have received a request to forget your  password, You can view Your password {user_data.password}'
                    # email_from =  settings.EMAIL_HOST_USER
                    # recipient_list = [user_data.email]
                    # send_mail(subject,message,email_from,recipient_list)
                    # message1 = ('Subject here', 'subratmohanty2309@gmail.com', ['ssubrat.m@gmail.com', ])
                    # # message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
                    # send_mass_mail((message1), fail_silently=False)
              
                    messages.success(request,"Login Successfully !!")
                    return redirect("home") 
                else:
                    messages.error(request,"Incorrect password !!") 
                    return redirect('login') 
            else:
                messages.error(request," Please enetr valid Email.. !!")
                return redirect('login') 
                
        return render(request,'Login.html')
    except Exception as e :
        print(e)

# Log-out  View Section >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

def logout(request):
    del request.session["id"]
    messages.success(request,'Logout Successfully !!')
    return redirect('login')

# profile View section>>>>>>>>>>>>>>>>>>>>>>>>>

def profile(request):
    login_user = User.objects.get(id = request.session["id"])
    print("login_user",login_user)

    address1 = Address.objects.filter(username=login_user.id)[0] 
    print("address-1",address1)

    address2 = Address.objects.filter(username=login_user.id).last 
    print("address-1",address2)
    return render(request,'Profile.html',{"user":login_user,"address1":address1,"address2":address2})

# Update Profile section >>>>>>>>>>>>>>>>>>>>>>

def profile_update(request,id):
    print("id",id)
    u_data = User.objects.get(id=id)
    print("userdata",u_data)
    if request.method == "POST":
        User.objects.filter(id = id).update(
            username = request.POST['username'],
            email = request.POST['email'],
            contact_number = request.POST['contact']
        )
        messages.success(request,"Profile Updated !!")
        return redirect('profile')
    return render(request,'Profile.html',{"user":u_data,"edit":True})








def address(request):
    if request.method == "POST":
        user_nam = User.objects.get(id = request.session['id'])
        contact_number = request.POST["contact_number"]
        city = request.POST["city"]
        area = request.POST['area']
        pin = request.POST["pincode"]
        state = request.POST["state"]
        user_address  = Address(username=user_nam,contact_number=contact_number,city=city,state=state,pincode=pin,area = area)
        user_address.save()
        return redirect("profile") 

    return render(request,'Address.html')

def forgetpassword(request):
    if request.method == "POST":
        email = request.POST[""]
    return render(request,'Forgetpassword.html')