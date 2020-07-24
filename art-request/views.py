from django.shortcuts import render
from artists.models import Artists

# Create your views here.

def artrequest(request):
    """ A view to return the request page """

    artists = Artists.objects.all()
    context = {
        'artists': artists,
    }

    return render(request, 'art-request/art-request.html', context)