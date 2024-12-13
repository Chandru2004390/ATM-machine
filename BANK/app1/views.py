from django.shortcuts import render,redirect
import random
from time import sleep,time
from app1.models import Users
from app1.programs import *
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'home.html')

def admin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        upassword=request.POST.get('upassword')
        if (username=='Chandru' or username=='chandru') and upassword=='chan@390':
            return redirect('add_del')
        else:
            res="Invalid Username or Password"
        return render(request,'admin.html',{'res':res})
    return render(request,'admin.html')

def tab(request):
    table=Users.objects.all()
    return render(request,'tab.html',{'table':table})

def add_del(request):
    return render(request,'add_del.html')


def generate_otp():
    return str(random.randint(1000, 9999))


def add(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pas=request.POST.get('pas')
        cpas=request.POST.get('cpas')
        pin=request.POST.get('pin')
        ph=request.POST.get('ph')
        bal=request.POST.get('bal')
        acc=request.POST.get('acc')
        con=request.POST.get('con')
        otp=request.POST.get('otp')
        if fname and pas and cpas and pin and ph:
            if ph.startswith('+'):
                if pas==cpas:
                    acc=int(ac())
                    if con=='otp':
                        otp=generate_otp()
                        request.session['otp']=otp
                        request.session['fname']=fname
                        request.session['lname']=lname
                        request.session['pas']=pas
                        request.session['cpas']=cpas
                        request.session['pin']=pin
                        request.session['ph']=ph
                        request.session['acc']=acc
                        res="OTP sent to your mobile number."
                        return render(request,'add.html',{'res':res,'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph,'acc':acc,'otp':otp,'bal':bal})
                    elif con=='verify':
                        if otp==request.session.get('otp'):
                            if bal:
                                try:
                                    bal=float(bal)
                                    if bal<0:
                                        res="Balance should be a positive amount."
                                        return render(request,'add.html',{'res':res,'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph,'bal':bal, 'acc': acc, 'otp': otp})
                                except ValueError:
                                    res="Invalid balance amount."
                                    return render(request,'add.html',{'res':res,'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph,'bal':bal,'acc':acc,'otp':otp})
                            else:
                                bal=0
                            Users.objects.create(First_Name=request.session['fname'],Last_Name=request.session['lname'],Password=request.session['pas'],Pin=request.session['pin'],Mobile_Number=request.session['ph'],Balance=bal,Acc_No=request.session['acc'])
                            messages.success(request, "User added successfully.")
                            return render(request, 'add_details.html', {'fname': request.session['fname'], 'lname': request.session['lname'], 'pas': request.session['pas'],'cpas': request.session['cpas'], 'pin': request.session['pin'], 'ph': request.session['ph'],'bal': bal, 'acc': request.session['acc']})
                        else:
                            res="OTP not correct. Please try again."
                            return render(request,'add.html', {'res':res,'fname':request.session['fname'],'lname': request.session['lname'],'pas':request.session['pas'],'cpas':request.session['cpas'],'pin':request.session['pin'],'ph': request.session['ph'],'bal':bal,'acc':request.session['acc'], 'otp': otp})
                else:
                    res="Password and Confirm Password do not match."
                    return render(request,'add.html',{'res':res,'fname':fname,'lname':lname,'pas': pas, 'cpas': cpas,'pin':pin,'ph':ph,'bal':bal,'acc':acc,'otp':otp})
            else:
                res="Enter mobile number with country code."
                return render(request,'add.html',{'res':res,'fname':fname,'lname':lname,'pas':pas, 'cpas': cpas,'pin':pin,'ph':ph,'bal':bal,'acc':acc,'otp':otp})
        else:
            res="All fields are required."
            return render(request,'add.html',{'res':res})
    return render(request,'add.html')




    '''
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pas=request.POST.get('pas')
        cpas=request.POST.get('cpas')
        pin=request.POST.get('pin')
        ph=request.POST.get('ph')
        bal=request.POST.get('bal')
        acc=request.POST.get('acc')
        con=request.POST.get('con')
        otp=request.POST.get('otp')
        if fname:
            if pas and cpas and pas==cpas:
                acc=int(ac())
                if bal=="":
                    bal=0
                    if con=='yes':
                        Users.objects.create(First_Name=fname,Last_Name=lname,Password=pas,Pin=pin,Mobile_Number=ph,Balance=bal,Acc_No=acc)
                        return render(request,'add_details.html',{'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph,'bal':bal,'acc':acc})
                    elif con=='otp':
                        res=ot()
                        return render(request,'add.html',{'res':res,'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph})

                        
                else:
                    bal=bal
                    Users.objects.create(First_Name=fname,Last_Name=lname,Password=pas,Pin=pin,Mobile_Number=ph,Balance=bal,Acc_No=acc)
                return render(request,'add_details.html',{'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph,'bal':bal,'acc':acc})
            else:
                res="Password Not Matching"
            return render(request,'add.html',{'fname':fname,'lname':lname,'pas':pas,'cpas':cpas,'pin':pin,'ph':ph,'bal':bal,'acc':acc,'res':res})
        else:
            res="You Entered Values Are Invalid"
        return render(request,'add.html',{'res':res})
    return render(request,'add.html')
    '''


def add_details(request):
    return render(request,'add_details.html')


def dell(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        acc=request.POST.get('acc')
        pas=request.POST.get('pas')
        ph=request.POST.get('ph')
        con=request.POST.get('con')
        
        if con=='Yes':
            if acc and pas and ph:
                Users.objects.get(Mobile_Number=ph,Password=pas,Acc_No=acc).delete()
                return redirect('add_del')
            else:
                res="You Entered Values Are Invalid"
            return render(request,'dell.html',{'res':res})
        return render(request,'add_del.html')
    return render(request,'dell.html')


def tab(request):
    table=Users.objects.all()
    return render(request,'tab.html',{'table':table})


def deposit(request):
    if request.method=='POST':
        acc=request.POST.get('acc')
        pas=request.POST.get('pas')
        user=Users.objects.filter(Acc_No=acc,Password=pas).first()
        if acc and pas:            
            if Users.objects.filter(Acc_No=acc,Password=pas):  
                return render(request,'depo.html',{'fname':user.First_Name,'lname':user.Last_Name,'acc':acc}) 
            else:
                res="Account Number and Password Notmatching...."
                return render(request,'deposit.html',{'res':res,'acc':acc,'pas':pas})
        else:
            res="Invalid"
        return render(request,'deposit.html',{'res':res,'acc':acc,'pas':pas})
    return render(request,'deposit.html')



def depo(request):
    if request.method=='POST':
        user=Users.objects.first()
        fname=user.First_Name
        lname=user.Last_Name
        amount=request.POST.get('amount')
        if amount:
            return render(request,'damount.html',{'amount':amount,'fname':fname,'lname':lname})
        else:
            res="Invalid"
            return render(request,'depo.html',{'amount':amount,'res':res})
    return render(request,'depo.html')



def damount(request):
    name=request.GET.get('name')
    acc=request.GET.get('acc')
    amount=request.GET.get('amount')
    if request.method=='POST':
        pin=request.POST.get('pin')
        if pin:
            user=Users.objects.filter(Acc_No=acc, Pin=pin).first()
            if user:
                try:
                    deposit_amount=float(amount)
                    if deposit_amount<0:
                        res="Enter a valid positive amount."
                        return render(request,'damount.html',{'res':res,'name':name,'acc':acc,'amount':amount})                    
                    user.Balance+=deposit_amount
                    user.save()
                    res=f"Deposit successful. Your new balance is {user.Balance}"
                except ValueError:
                    res="Enter a valid amount."
                return render(request,'damount.html',{'res':res,'name':name,'acc':acc,'amount':amount})
            else:
                res="Wrong Pin"
                return render(request,'damount.html',{'res':res,'name':name,'acc':acc,'amount':amount,'pin':pin})
        else:
            res="Invalid"
            return render(request,'damount.html',{'res':res,'name':name,'acc':acc,'amount':amount,'pin':pin})
    return render(request, 'damount.html', {'name': name, 'acc': acc, 'amount': amount})


def withdraw(request):
    if request.method=='POST':
        acc=request.POST.get('acc')
        pas=request.POST.get('pas')
        user=Users.objects.filter(Acc_No=acc,Password=pas).first()
        if acc and pas:            
            if Users.objects.filter(Acc_No=acc,Password=pas):  
                return render(request,'wepo.html',{'fname':user.First_Name,'lname':user.Last_Name,'acc':acc}) 
            else:
                res="Account Number and Password Notmatching...."
                return render(request,'withdraw.html',{'res':res,'acc':acc,'pas':pas})
        else:
            res="Invalid"
        return render(request,'withdraw.html',{'res':res,'acc':acc,'pas':pas})
    return render(request,'withdraw.html')

def wepo(request):
    if request.method=='POST':
        user=Users.objects.first()
        fname=user.First_Name
        lname=user.Last_Name
        amount=request.POST.get('amount')
        if amount:
            return render(request,'wamount.html',{'amount':amount,'fname':fname,'lname':lname})
        else:
            res="Invalid"
            return render(request,'wepo.html',{'amount':amount,'res':res})
    return render(request,'wepo.html')

def wamount(request):
    name=request.GET.get('name')
    acc=request.GET.get('acc')
    amount=request.GET.get('amount')
    if request.method=='POST':
        pin=request.POST.get('pin')
        if pin:
            user=Users.objects.filter(Acc_No=acc, Pin=pin).first()
            if user:
                try:
                    deposit_amount=float(amount)
                    if deposit_amount<0:
                        res="Enter a valid positive amount."
                        return render(request,'wamount.html',{'res':res,'name':name,'acc':acc,'amount':amount})                    
                    user.Balance-=deposit_amount
                    if user.Balance>0:
                        user.save()
                        res=f"Withdrawal successful. Now Your new balance is {user.Balance}"
                    else:
                        res="You Dont have that much of amount in your Account"
                    
                except ValueError:
                    res="Enter a valid amount."
                return render(request,'wamount.html',{'res':res,'name':name,'acc':acc,'amount':amount})
            else:
                res="Wrong Pin"
                return render(request,'wamount.html',{'res':res,'name':name,'acc':acc,'amount':amount,'pin':pin})
        else:
            res="Invalid"
            return render(request,'wamount.html',{'res':res,'name':name,'acc':acc,'amount':amount,'pin':pin})
    return render(request, 'wamount.html', {'name': name, 'acc': acc, 'amount': amount})


'''
    if request.method=='POST':
        acc=request.POST.get('acc')
        pas=request.POST.get('pas')
        if acc and pas:            
            if Users.objects.filter(Acc_No=acc,Password=pas):   
                return redirect('add_del')
            else:
                res="Account Number and Password Notmatching...."
                return render(request,'deposit.html',{'res':res})
        else:
            res="Invalid"
        return render(request,'deposit.html',{'res':res})
    return render(request,'deposit.html')
    
'''

def bal(request):
    if request.method=='POST':
        acc=request.POST.get('acc')
        pin=request.POST.get('pin')
        user=Users.objects.filter(Acc_No=acc,Pin=pin).first()
        if acc and pin:
            if user:
                res=f"Hello {user.First_Name} {user.Last_Name} Your Balance is ₹ {user.Balance}/-"
                return render(request,'bal.html',{'res':res,'acc':acc,'pin':pin,'fname':user.First_Name,'lname':user.Last_Name,'bal':user.Balance})
            else:
                msg="Account Number and Pin Not Matching"
                return render(request,'bal.html',{'msg':msg,'acc':acc,'pin':pin})
        else:
            msg="Invalid"
            return render(request,'bal.html',{'msg':msg,'acc':acc,'pin':pin})
    return render(request,'bal.html')

def pc(request):
    if request.method=='POST':
        con=request.POST.get('con')
        if con=='pin':
            return render(request,'pinc.html')
        elif con=='pas':
            return render(request,'pasc.html')
    return render(request,'pc.html')


def pinc(request):
    if request.method=='POST':
        set=request.POST.get('set')
        if set=='password':
            return render(request,'chpaspin.html')
        elif set=='old-pin':
            return render(request,'chpinpin.html')
        elif set=='otp':
            return render(request,'chotppin.html')
    return render(request,'pinc.html')


# Change Pin with password
def chpaspin(request): 
    if request.method=='POST': 
        acc=request.POST.get('acc') 
        pas=request.POST.get('pas') 
        new_pin=request.POST.get('new_pin') 
        user=Users.objects.filter(Acc_No=acc, Password=pas).first() 
        if user and len(new_pin)==4: 
            user.Pin=new_pin 
            user.save() 
            res="Pin changed successfully." 
            return render(request,'chpaspin.html',{'res':res,'acc':acc,'pas':pas,'new_pin':new_pin})
        else: 
            seter="Invalid details. Please try again." 
            return render(request, 'chpaspin.html', {'seter':seter,'acc':acc,'pas':pas,'new_pin':new_pin}) 
    return render(request, 'chpaspin.html')

# Change pin with old pin
def chpinpin(request):
    if request.method=='POST': 
        acc = request.POST.get('acc') 
        old_pin = request.POST.get('old_pin') 
        new_pin = request.POST.get('new_pin') 
        user = Users.objects.filter(Acc_No=acc, Pin=old_pin).first() 
        if user and len(new_pin) == 4: 
            user.Pin = new_pin 
            user.save() 
            res = "Pin changed successfully." 
            return render(request,'chpinpin.html',{'res':res})
        else: 
            seter = "Invalid details. Please try again." 
        return render(request, 'chpinpin.html', {'seter':seter}) 
    return render(request, 'chpinpin.html')


# change pin using OTP
def chotppin(request):
    context={
        'acc':'',
        'ph':'',
        'otp':'',
        'new_pin':'',
        'res':'',
        'otp_sent':False
    }
    if request.method=='POST':
        acc=request.POST.get('acc')
        ph=request.POST.get('ph')
        con=request.POST.get('con')
        otp=request.POST.get('otp')
        new_pin=request.POST.get('new_pin')
        context['acc']=acc
        context['ph']=ph
        if con=='send_otp':
            otp=generate_otp()
            request.session['otp']=otp
            request.session['acc']=acc
            request.session['ph']=ph
            print(f"OTP sent to {ph}: {otp}")
            context['res']=f"OTP sent to {ph}: {otp}"
            context['otp_sent']=True
        elif con=='change_pin':
            stored_otp=request.session.get('otp')
            if otp==stored_otp:
                user=Users.objects.filter(Acc_No=request.session.get('acc'), Mobile_Number=request.session.get('ph')).first()
                if user and len(new_pin)==4:
                    user.Pin=new_pin
                    user.save()
                    context['res']="Pin changed successfully."
                else:
                    context['res']="Invalid new pin. Please enter a 4-digit pin."
            else:
                context['res']="Invalid OTP. Please try again."
            context['otp_sent']=True
    return render(request,'chotppin.html',context)






def pasc(request):
    if request.method=='POST':
        set=request.POST.get('set')
        if set=='pin':
            return render(request,'chpaspin.html')
        elif set=='old-pas':
            return render(request,'chpaspas.html')
        elif set=='otp':
            return render(request,'chotppas.html')
    return render(request,'pasc.html')

# Change Password with old-password
def chpaspas(request):
    if request.method=='POST': 
        acc=request.POST.get('acc') 
        pas=request.POST.get('pas') 
        new_pas=request.POST.get('new_pas') 
        user=Users.objects.filter(Acc_No=acc, Password=pas).first() 
        if user and new_pas: 
            user.Password=new_pas
            user.save() 
            res="Password changed successfully." 
            return render(request,'chpaspas.html',{'res':res,'acc':acc,'pas':pas,'new_pas':new_pas})
        else: 
            seter="Invalid details. Please try again." 
            return render(request, 'chpaspas.html', {'seter':seter,'acc':acc,'pas':pas,'new_pas':new_pas}) 
    return render(request, 'chpaspas.html')

# change password with pin
def chpinpas(request):
    if request.method=='POST': 
        acc=request.POST.get('acc') 
        pin=request.POST.get('pin') 
        new_pas=request.POST.get('new_pas') 
        user=Users.objects.filter(Acc_No=acc, Pin=pin).first() 
        if user and len(pin)==4: 
            user.Password=new_pas 
            user.save() 
            res="Password changed successfully." 
            return render(request,'chpinpas.html',{'res':res})
        else: 
            seter="Invalid details. Please try again." 
        return render(request, 'chpinpas.html', {'seter':seter,'acc':acc,'pin':pin,'new_pas':new_pas}) 
    return render(request, 'chpinpas.html')

# change password with otp
def chotppas(request):
    context={
        'acc':'',
        'ph':'',
        'otp':'',
        'new_pas':'',
        'res':'',
        'otp_sent':False
    }
    if request.method=='POST':
        acc=request.POST.get('acc')
        ph=request.POST.get('ph')
        con=request.POST.get('con')
        otp=request.POST.get('otp')
        new_pas=request.POST.get('new_pas')
        context['acc']=acc
        context['ph']=ph
        if con=='send_otp':
            otp=generate_otp()
            request.session['otp']=otp
            request.session['acc']=acc
            request.session['ph']=ph
            print(f"OTP sent to {ph}: {otp}")
            context['res']=f"OTP sent to {ph}: {otp}"
            context['otp_sent']=True
        elif con=='change_pas':
            stored_otp=request.session.get('otp')
            if otp==stored_otp:
                user=Users.objects.filter(Acc_No=request.session.get('acc'), Mobile_Number=request.session.get('ph')).first()
                if user and new_pas:
                    user.Pin=new_pas
                    user.save()
                    context['res']="Password changed successfully."
                else:
                    context['res']="Invalid new Password"
            else:
                context['res']="Invalid OTP. Please try again."
            context['otp_sent']=True
    return render(request,'chotppas.html',context)
