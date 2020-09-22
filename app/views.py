from django.shortcuts import render,redirect
from .models import items
from .forms import Itemsform
from django.db.models import Sum

# Create your views here.
def home(request):
    
    if request.method != 'POST':
        
        print(request.method)
        form=Itemsform()
    else:
        a=request.POST.get('item')
        b=request.POST.get('quantity')
        d=request.POST.get('rate')
        h=request.POST.get('hsn')
        number1=int(d)
        number=int(b)
        c=number*number1

        items.objects.create(itemname=a,hsn=h,quantity=b,rate=d,price=c)
        return render(request,'home.html')
    context={'form':form}
    print('prani',form.errors)
    return render(request,'home.html',context)

def total(request):
 
    
    a=items.objects.all()
    b=items.objects.count()
    c=items.objects.aggregate(Sum('price'))
    for i,j in c.items():
        total=j
    

    return render(request,'total.html',{'del':a,'count':b,'total':total})


def delete(request,id):
    val=items.objects.get(id=id)
    val.delete()
    return redirect('keeper:total')

def remove(request):
    val=items.objects.all()
    val.delete()
    a="Success"
    return redirect('keeper:home')


from django.views.generic import View
from .render import Render
import datetime

def convertToDigit(n, suffix):
    EMPTY = ""

    X = [EMPTY, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
         "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
         "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
         "Seventeen ", "Eighteen ", "Nineteen "]

    Y = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
         "Sixty ", "Seventy ", "Eighty ", "Ninety "]
    # if n is zero
    if n == 0:
        return EMPTY

    # split n if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix
def convert(n):

    # add digits at ten millions & hundred millions place
    result = convertToDigit((n // 1000000000) % 100, "Billion, ")

    # add digits at ten millions & hundred millions place
    result += convertToDigit((n // 10000000) % 100, "Crore, ")

    # add digits at hundred thousands & one millions place
    result += convertToDigit(((n // 100000) % 100), "Lakh, ")

    # add digits at thousands & tens thousands place
    result += convertToDigit(((n // 1000) % 100), "Thousand ")

    # add digit at hundreds place
    result += convertToDigit(((n // 100) % 10), "Hundred ")

    if n > 100 and n % 100:
        result += "and "

    # add digits at ones & tens place
    result += convertToDigit((n % 100), "")

    return result



class Pdf(View):

    def get(self, request):
        a=items.objects.all()
        b=items.objects.count()
        c=items.objects.aggregate(Sum('price'))
        name=request.GET.get('fname')
        money=request.GET.get('type')
        address=request.GET.get('address')
        tax=request.GET.get('cost')
        vnum=request.GET.get('vnumber')
        sname=request.GET.get('supply')
        n1=request.GET.get('number')
        for i,j in c.items():
            total=j
        if money=='With in State':
            f='gst'
            e=0.025
            t=total*e
            ta=t*2
            d=total+ta
        elif money=='Other State':
            f='ist'
            e=0.18
            t=total*e
            ta=t
            d=total+t           
        d=int(d)+int(tax)
        r=round(d)
        w=convert(r)
        x=w.upper()
        today = datetime.datetime.now().strftime('%m/%d/%y')
        params = {
            'del':a,'count':b,'total':total,'name':name,
            'request': request,'stats':t,'search':f,'total1':d,'address':address,'n1':n1,'word':x,'date':today,'cost':tax,'cost1':ta,'vnum':vnum,'sname':sname
        }
        return Render.render('pdf.html', params)