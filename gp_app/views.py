from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Business
from .forms import BusinessForm
from django.contrib import messages

# Create your views here.
def indexCity(request, city):
    businesses_in_city = Business.objects.filter(city = city)
    context = {'businesses_in_city':businesses_in_city}
    print("Businesses near you", businesses_in_city)
    return render( request, 'gp_app/index_city.html', context)

def index(request):
    #all_cities = City.objects.filter()
    CITIES = (' ','Colorado Springs','Denver', 'Fort Collins')
    return render(request, 'gp_app/index.html', {'cities': CITIES})

class BusinessDetailView(generic.DetailView):
    model = Business

def deleteBusiness(request, business_id):
    business = Business.objects.get(id=business_id)
    context = {'business': business}
    if request.method == 'GET':
        return render(request, 'gp_app/business_delete.html',context)       
    elif request.method == 'POST':
        business.delete()
        return redirect('index')
    
def createBusiness(request):
    form = BusinessForm()
    #business = Business.objects.get(pk=business_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        business_data = request.POST.copy()
        #business_data['business_id'] = business_id
        
        form = BusinessForm(business_data)
        if form.is_valid():
            # Save the form without committing to the database
            business = form.save(commit=False)
            # Set the portfolio relationship
            business.save()

            # Redirect back to the portfolio detail page
            return redirect('index')

    context = {'form': form}
    return render(request, 'gp_app/business_form.html', context)

def updateBusiness(request, business_id):
    business = Business.objects.get(id=business_id)
    #student = Customer.objects.get(portfolio_id=portfolio_id)
    form = BusinessForm(instance=business)
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            business.save()

            # Redirect back to the business detail page
            return redirect('business-detail', business_id)
    else:
        context = {'form': form}
        return render(request, 'gp_app/business_form.html', context) 
