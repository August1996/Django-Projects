from django.views import generic
from items.models import Item,Photo

class IndexView(generic.ListView):
    template_name = 'index.html'
    def get_queryset(self):
        return Item.objects.all()[:5]

class ListView(generic.ListView):
    template_name = 'list_items.html'
    model = Item

class ItemDetailView(generic.DetailView):
    template_name = 'items_detail.html'
    model = Item

class PhotoDetailView(generic.DetailView):
    template_name = 'photos_detail.html'
    model = Photo