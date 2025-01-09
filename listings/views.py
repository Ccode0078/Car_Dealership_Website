from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .forms import ListingForm

# Query request from model       
def listings(request):
    # Retrieve all listing objects from the database
    all_listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': all_listings})

# Function to display details of a single listing
def listing(request, id):
    # Retrieve a specific Listing object based on the provided id
    listing = Listing.objects.get(id=id)
    # Pass the retrieved listing to the template through context
    context = {'listing': listing}
    return render(request, 'listing.html', context)

# Function to create a new listing
def create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create.html', context)

def update(request, id):
    listing = Listing.objects.get(id=id)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update.html', context)

# Function to remove a listing
def delete(request, id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect('/')

# Header
def index(request):
    listings = Listing.objects.all()
    Num_of_Listings = Listing.objects.all().count()
    context = {'listings': listings, 'Num_of_Listings': Num_of_Listings}
    return render(request, 'index.html', context)

# Vehicle page
def Vehicles(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'vehicle.html', context)

def listing_detail(request, id):
    print(f"Accessed listing with ID: {id}")
    listing = get_object_or_404(Listing, id=id)
    images = listing.images.all()
    return render(request, 'listing.html', {'listing': listing, 'images': images})







def car_details(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'car_details.html', {'car': listing})


def carousel_test(request):
    return render(request, 'carousel_test.html')




# def listings(request):
#     #Retrive all listing objects from the database
#     listings = Listing.objects.all()
#    # Pass the retrieved listing to the template through context
#     context = {
#         'listings':listings
#     }
#      # Render the 'listings.html' template with the context data
#     return render(request,'listings.html',context)