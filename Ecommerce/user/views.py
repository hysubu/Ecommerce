from django.shortcuts import render,redirect,HttpResponse
from cryptography.fernet import Fernet
from user .models import User,Address
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import json
from product import views
# from user import serializer
# Create your views here.


# user Signup Section ..........

def Usersignup(request):
    try:
        if request.method == "POST":
            fname = request.POST["firstname"]
            password = request.POST["password"]
            confirm_pass = request.POST["confirm-password"]
            contact = request.POST["contactnumber"]
            email = request.POST["email"]
            p_photo = request.FILES['profile_photo']
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
            try :
                if password == confirm_pass :
                    user = User(first_name = fname,password = encpassword.decode('utf-8'),password_key = passwordkey.decode('utf-8'),email = email,profile_photo = p_photo,contact_number = contact )
                    user.save()
                    messages.success(request,'Registration Successfully .. !!')
            except :
                messages.error(request,"")
        
        return render(request,'Customeregistration.html')
    except :
        messages("error 404 ")


# User Login section ..............

def userlogin(request):    
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
                session_id = request.session["u_id"] = user_data.first_name
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

# def jsn_data(data):
#     data = serializers.serialize('json', data)
#     return HttpResponse(data, content_type="application/json")

# User Logout Section...........

def userlogout(request):
    del request.session["u_id"]
    messages.success(request,'Logout Successfully !!')
    return redirect('login')


def change_password(request):
    if request.method == "POST":
        old_password = request.POST["old-password"]
        new_pssword = request.POST["new-password"]
    return render(request,"Changepassword.html")


def forgetpassword(request):
    if request.method == "POST":
        email = request.POST["email"]
        user_data = User.objects.get(email=email)
        print(user_data)
        user_pass = user_data.password
        print("password",user_pass)
        fernet = Fernet(user_data.password_key)
        print("fernate::-",fernet)
        decpassword = fernet.decrypt(user_data.password).decode()
        print("decordpassword:--",decpassword) 
        
        subject = ""
        message = f'Hi {user_data.first_name} we have received a request to forget your  password, You can view Your password {decpassword}'
        # email_from =  settings.EMAIL_HOST_USER
        # recipient_list = [user_data.email]
        first_name = user_data.first_name
        last_name = user_data.last_name

        html_template = render_to_string("email.html",{
            'firstname':first_name,
            'lastname' : last_name,
            "password": decpassword
        })
        # html_message = render_to_string(html_template,{"username":username})
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [user_data.email]
        send_mail(subject,message,email_from,recipent_list,html_message=html_template)
        return redirect('home')
    return render(request,'forgetpassword.html')
    # from django.core.mail import EmailMultiAlternatives

# subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
# text_content = 'This is an important message.'
# html_content = '<p>This is an <strong>important</strong> message.</p>'
# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# msg.attach_alternative(html_content, "text/html")
# # msg.send()
        # if user_data:
        #     # # password_key = user_data.password_key
        #     # # print(password_key)
        #     # fernet = Fernet(user_data.password_key)
        #     # print("fernate::-",fernet)
        #     # # encpassword = fernet.encrypt(l_pass.encode())
        #     # decpassword = fernet.decrypt(user_data.password).decode()
        #     # print("decordpassword:--",decpassword)
        #     old_passwordkey = Fernet.generate_key()
        #     print("password_key ::--",old_passwordkey)
        #     fernet = Fernet(old_passwordkey)
        #     print("fernate:--",fernet)
        #     encpassword = fernet.encrypt(new_pass.encode())
        #     print("encrypt_pass::==", encpassword)
        #     User.objects.filter(email=user_data).update(
        #         passwordkey = request.POST[old_passwordkey],
        #         password = request.POST[encpassword]
        #     )   
        #     return redirect("home") 

# Profile Data  View >>>>>>>>>>> 

def profile(request):
    user = User.objects.get(id = request.session['id'])
    user_add = user.id

    user_address = Address.objects.filter(username = user_add)
    user_address2 = Address.objects.filter(username = user_add).last
    print(user_address)
    return render(request,'Profile.html',{"user":user,"address":user_address,"address2":user_address2})


# Profile Update >>>>>>>>>>>>>>>>>>>>>>>>>>>>.

def profile_update(request,id):
    u_data = User.objects.get(id=id)
    if request.method == "POST":
        User.objects.filter(id = id).update(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            contact_number = request.POST['contact_number'],
            # profile_photo = request.FILES['profile']
        )
        messages.success(request,"Profile Updated !!")
        return redirect('profile')
    return render(request,'Profile.html',{"user":u_data,"edit":True})



#  Save Address >>>>>>>>>>>>>>>>>.

def user_address(request):
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


# Address View >>>>>>>>>>>>>>>>>>>>

def view_address(request,id):
    print("user-address",user_address)
    return render(request,'Profile.html',{})





  