import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query, EditorsPick
from home.models import HomePage

def get(request, university, language):
    filtered_pages = HomePage.objects.live().filter(language=language, university=university)

    response_data = []
    for page in filtered_pages:
        callback = request.GET['callback']
        response_data.append({
            'section_1': page.section_1,
            'section_2': page.section_2,
            'section_3': page.section_3,
            'section_4': page.section_4,
            'section_5': page.section_5,
            'section_6': page.section_6
        })

    return HttpResponse(callback + '(' + str(json.dumps(response_data))+ ')')