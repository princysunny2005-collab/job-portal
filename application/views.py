from django.shortcuts import render,redirect,get_object_or_404
from .models import RegisterModel
from .forms import RegisterModelForms,UpdateForm


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request,"home.html")
def header(request):
    return render(request,"header.html")
def footer(request):
    return render(request,"footer.html")
def base(request):
    return render(request,"base.html")
def category(request):
    return render(request,"category.html")
def find(request):
    return render(request,"find.html")
def career(request):
    return render(request,"career.html")
def login(request):
    return render(request,"login.html")
def register(request):
    if request.method == "POST":
        mydata = RegisterModelForms(request.POST,request.FILES)
        if mydata.is_valid():
            user = mydata.save()
            fullname = mydata.cleaned_data["fullname"]
            email = mydata.cleaned_data["email"]
            subject ="Job Registration is Sccessfull"
            message =f"""
                        Hello {fullname},
                        Your Registration is successfully compleated
                        Thank You for choosing us,
                    """
            send_mail(subject,message,
                      settings.DEFAULT_FROM_EMAIL,[email],fail_silently=False)
            messages.success(request,"Registraion Successful")
    else:
            mydata =RegisterModelForms()
            print("saved")
        # profilepic =request.FILES.get("profilepic")
        # fullname =request.POST.get("fullname")
        # email =request.POST.get("email")
        # password =request.POST.get("password")
        # number =request.POST.get("number")
        # cv =request.FILES.get("cv")

        # mydata =RegisterModel(
        #     profilepic =profilepic,
        #     fullname =fullname,
        #     email =email,
        #     password =password,
        #     number =number,
        #     cv =cv
        # )
        # mydata.save()
        # print("saved")

    return render(request,"register.html")

def dashboard(request):
    data =RegisterModel.objects.all()
    return render(request,"dashboard.html",{"data":data})

def update(request,pk):

    user=get_object_or_404(RegisterModel,id=pk)
    if request.method == "POST":
        forms =RegisterModel(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
    else:
        forms.UpdateForm(instamnce=user)
        # profilepic =request.FILES.get("profilepic")
        # fullname =request.POST.get("fullname")
        # email =request.POST.get("email")
        # password =request.POST.get("password")
        # cv =request.POST.get("cv")


        # mydata.save()
        # print("saved")
    return render(request,"update.html",{"data":forms})

# def register_view(request):
#     if request.method == "POST":
#         form=RegisterViewForm(request.POST)
#         if form.is_valid:
#             form.save()
#             print("saved")
#     return render(request,"register_view.html")

def profile(request):
    if not request.session.get("user_id"):
        return redirect("login")
    data = RegisterModel.objects.get(id=request.session["user_id"])
    return render(request,"profile.html",{"data":data})

def logout(request):
    response = redirect("login")
    response.delete_cookie("username")
    response.delete_cookie("fullname")
    return response