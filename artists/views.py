from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Category
from .models import Artists

# Create your views here.
def all_artists(request):
    """ A view to show all products, including sorting and search queries """

    artists = Artists.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                artists = artists.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artists = artists.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            artists = artists.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('artists'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            artists = artists.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'artists': artists,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'artists/artists.html', context)


def artist_details(request, artist_id):
    """ A view to show individual product details """

    artists = get_object_or_404(Artists, id=artist_id)

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artist-details.html', context)
