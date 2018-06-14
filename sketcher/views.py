# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import json
import requests
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

def sketch(request):
    response = ""
    return render(request, 'index.html', {})

def suggestions(request):
    queried = request.GET.get("q", "")
    queried = queried.strip() 
    response_data = {}
    if queried == "":
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    suggested_images = get_suggested_images(queried)
    response_data['images'] = suggested_images
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_suggested_images(query):
    data = {"pageUri":"/search?q=%s&page=1" % query}
    headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0 FKUA/website/41/website/Desktop",
            "sn":"2.VIF4EE7CBA860E4B43B6CE95FC6AD95C0B.SIBCE1A10845154B3994F8915DC5056A45.VSB5A5BDC8A708493D9FAAC735594B5D44.1498657291",
            "Content-Type":"application/json"
            }
    data = json.dumps(data)
    _post_data = requests.post('http://mobileapi.flipkart.net/4/page/fetch', data = data, headers = headers)
    response = _post_data.json()['RESPONSE']
    slots = response['slots']
    for _slot in slots:
        if _slot['slotType'] == 'WIDGET':
            facet_response = _slot['widget']['data']['filters']['facetResponse']
            titles = get_titles(facet_response)

    return {'titles' : titles}


def get_titles(facet_response):
    titles = []
    if 'storeMetaInfoList' in facet_response:
        for meta in facet_response['storeMetaInfoList']:
            title = meta['title'].lower()
            if title.endswith('s'):
                title = title[:-1]
            titles.append(title)
    return titles
