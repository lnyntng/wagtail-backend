import json

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query, EditorsPick

def get(request, category):
    filtered_pages = []

    if category is 'signature':
    	filtered_pages = HomePage.objects.live().filter(category='signature')
    elif category is 'discover':
    	filtered_pages = HomePage.objects.live().filter(category='discover')
    else:
    	filtered_pages = HomePage.objects.live()

    response_data = []
    for page in filtered_pages:
    	for rawhtml in page.body:
    		response_data.append({'content': body, 'tags': category})

    return HttpResponse(json.dumps(response_data), content_type="application/json")