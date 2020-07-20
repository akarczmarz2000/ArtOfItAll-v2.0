from django.contrib import admin
from .models import Artists

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price_range',
        'rating',
        'request',
    )

    ordering = ('name',)


admin.site.register(Artists, ArtistAdmin)
