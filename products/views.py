from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Region, ProductImage
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A main view to see all available products and filter options """

    products = Product.objects.all()
    regions = Region.objects.all()
    query = None
    region_query = None
    region_query_name = None
    sort = None
    direction = None
    current_sorting = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'new':
                sortkey = 'new_product'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            if sortkey == 'new_product':
                products = products.filter(new_product=True)
                sort = 'new'
                direction = None
            else:
                products = products.order_by(sortkey)

        if 'region' in request.GET:
            region_query = request.GET['region'].split()
            products = products.filter(region__name__in=region_query)
            region_query = Region.objects.filter(name__in=region_query)
            region_query_name = region_query[0].name

        if 'search-query' in request.GET:
            query = request.GET['search-query']
            if not query:
                messages.error(request, 'You did not entery any search critereia' )
                return redirect(reverse('products'))
            
            search_queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(description_2__icontains=query) | Q(roast_level__icontains=query) | Q(region__friendly_name__in=query)
            products = products.filter(search_queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'regions': regions,
        'search_query': query,
        'region_query':region_query,
        'region_query_name': region_query_name,
        'current_sorting': current_sorting,
    }
    return render (request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product's page """

    product = get_object_or_404(Product, pk=product_id)
    image_list = product.other_images.all()

    context = {
        'product': product,
        'image_list': image_list,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            # return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
