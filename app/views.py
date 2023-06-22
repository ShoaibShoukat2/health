from django.shortcuts import render,redirect
from .models import Myform
# Create your views here.

def index(request):
    data  = Myform.objects.all()

    context = {
        'mydata':data
    }
    return render(request,'index.html',context)


def results(request):
    return render(request,'results.html')


    # form data
def form(request):
    if request.method == 'POST':
        first_value = request.POST.get('Acidity_1_ph')
        second_value = request.POST.get('quantity_1_grams')
        third_value = request.POST.get('Acidity_2_ph')
        fourth_value = request.POST.get('quantity_2_grams')
        fifth_value = request.POST.get('Acidity_3_ph')
        sixth_value = request.POST.get('quantity_3_grams')
        seventh_value = request.POST.get('over_all_food')

        # calculation

        result_data = (float(first_value)*float(second_value)+float(third_value)*float(fourth_value)+float(fifth_value)*float(sixth_value))/float(seventh_value)
        
        form_data = Myform(
            acidity1=float(first_value),
            quantity1=float(second_value),
            acidity2=float(third_value),
            quantity2=float(fourth_value),
            acidity3=float(fifth_value),
            quantity3=float(sixth_value),
            total=float(seventh_value),
            result = float(result_data)
        )

        if form_data:
           form_data.save() 
           return redirect('data.html')
    return render(request,'form.html')

def show_data(request):
    data  = Myform.objects.all()

    context = {
        'mydata':data
    }

    return render(request,'data.html',context)
