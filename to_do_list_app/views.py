from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader


# Create your views here.

def index(request):
    template = loader.get_template('to_do_list_app/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def lists(request):
    # lists = Stock.objects.all()
    template = loader.get_template('to_do_list_app/lists.html')
    context = {
        'lists': [],
    }
    return HttpResponse(template.render(context, request))


def list_detail(request, list_id):
    # stock = Stock.objects.filter(id=company_id).first()

    context = {
        'list': [],
    }
    template_name = 'to_do_list_app/detail.html'
    return render(request, template_name, context)
