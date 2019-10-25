from datetime import timezone, date, datetime
from xmlrpc.client import DateTime

from django.db.models import DateTimeField
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from to_do_list_app.models import List, Item


# Create your views here.

def index(request):
    template = loader.get_template('to_do_list_app/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


class Lists(ListView):
    model = List


class Detail_list(DetailView):
    model = List


class Create_list(CreateView):
    model = List
    form = List
    fields = "__all__"

    def get_success_url(self):
        return reverse('lists')  # Redireccionamos a la vista principal 'leer'


def list_detail(request, list_id):
    list = List.objects.get(id=list_id)
    list.item_set.all()
    context = {
        'list': list,
    }
    template_name = 'to_do_list_app/detail.html'
    return render(request, template_name, context)


def item_delete(request, list_id, item_id):
    item_to_delete = Item.objects.get(id=item_id)
    print("Deleting item with text:", item_to_delete.text)
    item_to_delete.delete()
    reverse('lists')


def item_add(request, list_id):
    text = request.POST.get('item_text')
    print("Adding item with text:", text)
    new_item = Item(list_id=list_id, text=text, creation_date=datetime.today())
    new_item.save()
    reverse('lists')


def list_add(request):
    title = request.POST.get('list_title')
    print("Adding list with title:", title)
    new_list = List(title=title, creation_date=datetime.today())
    new_list.save()
    reverse('lists')


def list_delete(request, list_id):
    list_to_delete = List.objects.get(id=list_id)
    print("Deleting list with title", list_to_delete.title)
    list_to_delete.delete()
    reverse('lists')
