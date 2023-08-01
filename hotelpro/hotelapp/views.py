from django.shortcuts import render,redirect
from . models import Hotels,Comment
from . forms import BookingForm
from . forms import TodoForm


# Create your views here.\
def update(request,update_id):
    tasks = Comment.objects.get(id=update_id)
    form = TodoForm(request.POST or None, instance=tasks)
    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/cmnt")
    return render(request,'update.html',{'form':form})
def delete(request,delete_id):
    tasks = Comment.objects.get(id=delete_id)
    tasks.delete()
    return redirect("http://127.0.0.1:8000/cmnt")

def index(request):
    product = Hotels.objects.all()
    item = {
        'product':product
    }
    return render(request,'index.html',item)

def comments(request):
    cmnt = Comment.objects.all()
    obj = {
        'cmnts':cmnt
    }
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('comen')
        abc = Comment(name=name,desc=desc)
        abc.save()
    return render(request,'comments.html',obj)



   

def booking(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
      

    form =BookingForm()
    forms = {
        'form':form
    }    
    return render(request,'booking.html',forms)
