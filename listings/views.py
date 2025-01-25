from django.shortcuts import render, redirect,get_object_or_404
from .forms import ListingForm, ImageForm
from .models import Listing, Image

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




def create_listing(request):
    if request.method == 'POST':
        listing_form = ListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            listing = listing_form.save()
            print(f"Listing created: {listing.name}")
            for file in request.FILES.getlist('images'):
                print(f"Handling file: {file.name}")  # Debugging print statement
                try:
                    image_instance = Image.objects.create(listing=listing, image=file)
                    print(f"Image saved: {image_instance.image.url}")  # Debugging print statement
                except Exception as e:
                    print(f"Error saving file {file.name}: {e}")  # Error debugging
            return redirect('listing_detail', id=listing.id)
        else:
            print("Form is not valid")  # Debugging print statement
    else:
        listing_form = ListingForm()
        print("GET request")  # Debugging print statement
    return render(request, 'create_listing.html', {
        'listing_form': listing_form,
    })












def update(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            # Handling extra images
            images = request.FILES.getlist('extra_images')
            for image in images:
                Image.objects.create(listing=listing, image=image)
            return redirect('update', id=listing.id)
    else:
        form = ListingForm(instance=listing)
    context = {'form': form, 'car': listing, 'images': listing.images.all()}
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
    for image in images:
        print(f"Image: {image.image.url}")  # Debugging print statement
    return render(request, 'car_details.html', {'car': listing, 'images': images})








def car_details(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    images = listing.images.all()
    return render(request, 'car_details.html', {'car': listing, 'images':images})


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