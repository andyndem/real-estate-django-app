from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Listing
from .forms import ListingForm


# Create your views here.
# CRUD - create, retrieve, update, delete, list

def listing_list(request):
  listings = Listing.objects.all()
  context = {
    "listings": listings
  }
  return render(request, "listings/listings.html", context)

def listing_retrieve(request, pk):
  listing = Listing.objects.get(id=pk)
  context = {
    "listing": listing
  }
  return render(request, "listings/listing.html", context)

def listing_create(request):
  form = ListingForm()
  if request.method == "POST":
    form = ListingForm(request.POST, request.FILES)
    # print(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/")
    
  context = {
    "form": form
  }
  return render(request, "listings/listing-create.html", context)



def listing_update(request, pk):
  listing = Listing.objects.get(id=pk)
  form = ListingForm(instance=listing)
  if request.method == "POST":
    listing = Listing.objects.get(id=pk)
    form = ListingForm(request.POST, instance=listing)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/")
    
  context = {
    "form": form
  }
  return render(request, "listings/listing-update.html", context)




# Bad code..form cannot prepopulate
# # update view for details
# def listing_update(request, pk):
#   # Prepolulate the form
#   listing = get_object_or_404(Listing, id = pk)
#   form = ListingForm(instance=listing)
#   # dictionary for initial data with field names as keys
#   # context ={}
# 	# fetch the object related to passed id
#   listing = get_object_or_404(Listing, id = pk)
# 	# pass the object as instance in form
#   form = ListingForm(request.POST or None, instance = listing, files=request.FILES)
# 	# save the data from the form and
# 	# redirect to detail_view
#   if form.is_valid():
#     form.save()
#     return HttpResponseRedirect("/")

# 	# add form dictionary to context
#   context = {
#     "form": form
#   }
#   return render(request, "listings/listing-update.html", context)






def listing_delete(request, pk):
  listing = Listing.objects.get(id=pk)
  listing.delete()
  return redirect("/")


