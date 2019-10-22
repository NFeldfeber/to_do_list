from datetime import timezone, date, datetime
from xmlrpc.client import DateTime

from django.db.models import DateTimeField
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader
from to_do_list_app.models import List, Item


# Create your views here.

def index(request):
    template = loader.get_template('to_do_list_app/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def lists(request):
    lists = List.objects.all()
    template = loader.get_template('to_do_list_app/lists.html')
    context = {
        'lists': lists,
    }
    return HttpResponse(template.render(context, request))


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
    return lists(request)


def item_add(request, list_id):
    text = request.POST.get('item_text')
    print("Adding item with text:", text)
    new_item = Item(list_id=list_id, text=text, creation_date=datetime.today())
    new_item.save()
    return lists(request)


def list_add(request):
    title = request.POST.get('list_title')
    print("Adding list with title:", title)
    new_list = List(title=title, creation_date=datetime.today())
    new_list.save()
    return lists(request)


def list_delete(request, list_id):
    list_to_delete = List.objects.get(id=list_id)
    print("Deleting list with title", list_to_delete.title)
    list_to_delete.delete()
    return lists(request)
