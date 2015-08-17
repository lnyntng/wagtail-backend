import json
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query, EditorsPick
from home.models import HomePage, ArticlePage

def get(request, university, language):
    filtered_pages = HomePage.objects.live().filter(language=language, university=university)
    callback = request.GET['callback']

    response_data = []
    for page in filtered_pages:        
        response_data.append({
            'section_1': page.section_1,
            'section_2': page.section_2,
            'section_3': page.section_3,
            'section_4': page.section_4,
            'section_5': page.section_5,
            'section_6': page.section_6
        })

    return HttpResponse(callback + '(' + str(json.dumps(response_data))+ ')')


def articles(request, university):
    filtered_pages = ArticlePage.objects.live().filter(university=university)
    callback = 'sdkajdalk' #request.GET['callback']

    response_data = []
    for page in filtered_pages:
        for article in page.articles:            
            article_dictionary = dict(zip(article.value.keys(), article.value.values()))
            article_dictionary['body'] = article_dictionary['body'].source
            response_data.append(article_dictionary)

    return HttpResponse(callback + '(' + str(json.dumps(response_data))+ ')')