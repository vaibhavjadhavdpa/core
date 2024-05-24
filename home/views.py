from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
   #return HttpResponse("<h1>Hey, This is Home Page</h1>")
   peoples = [
      {'name' : 'Kaushal Gupta', 'age' : 22},
      {'name' : 'Saurabh Nimse', 'age' : 24},
      {'name' : 'Gayatri More', 'age' : 26},
      {'name' : 'Rohit Nardela', 'age' : 27},

   ]
   vegetables = ['Pumkin','Tomato', 'Potatoe']

   text="""lorem dsfasf asddASDS Asdsasd ADAS wadADASD asdASDasd ASSDASd ASSDSA ASDasdsa ASDSa adASDASD asdsASD FSS ADDF ADFSDFD""";
   context={'page':'Home'}
   return render(request , "index.html", context = {'page':'Home','peoples' : peoples,'vegitables':vegetables,'text':text })
   
   #return render(request , "index.html")

def index(request):
   context={'page':'Home'}
   return render(request , 'index.html',context)

def aboutus(request):
   context={'page':'Aboutus'}
   return render(request , 'aboutus.html', context)

def contact(request):
   context={'page':'Contactus'}
   return render(request , 'contact.html',context)

 
def success_page(request):
    context={'page':'Success Page'}
    return HttpResponse("<h1>Hey, This is Success Page</h1>",context)
    
