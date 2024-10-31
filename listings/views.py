from django.shortcuts import render,redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.
#like functions

#Query request from model
def listings(request):
    #Retrive all listing objects from the database
    listings = Listing.objects.all()
   # Pass the retrieved listing to the template through context
    context = {
        'listings':listings
    }
     # Render the 'listings.html' template with the context data
    return render(request,'listings.html',context)

# Function to display details of a single listing
def listing(request,id):
     # Retrieve a specific Listing object based on the provided id
    listing = Listing.objects.get(id=id)
     # Pass the retrieved listing to the template through context
    context = {
        'listing': listing
    }
    # Render the 'listing.html' template with the listing details
    return render(request,'listing.html',context)

# Function to create a new listing
def create(request):
    form = ListingForm()
    # Check if the request is a POST request (form submission)
    if request.method == 'POST':
        # Bind form data from the POST request to the form instance
        form = ListingForm(request.POST,request.FILES)
         # Validate the form data
        if form.is_valid:
            #Save form to create new object
            form.save()
            # return to homepage after saving
        return redirect('/')
    context = {
        'form': form
    }
    return render(request,'create.html',context)

def update(request,id):
    listing = Listing.objects.get(id=id)
    # Create an instance of ListingForm pre-filled with the data of the retrieved listing
    form = ListingForm(instance = listing)
    if request.method == 'POST':
     # Bind the submitted form data to the form instance, with existing data from the listing
        form = ListingForm(request.POST,instance = listing,files=request.FILES)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request,'update.html',context)
#function to remove a listing
def delete(request,id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect('/')
