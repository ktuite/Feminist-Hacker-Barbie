from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext
from django.db import connection, transaction
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required


from settings import PREVENT_UPLOADS, HIDE_FRONT_PAGE, IMGUR_CLIENT_ID

from models import *

import random
import json

def index(request):

    if not HIDE_FRONT_PAGE:
        # On the live site, I only show "endorsed" panels on the front page
        #adaptations = Adaptation.objects.filter(endorsed=True).order_by("?")[:15]
        adaptations = Adaptation.objects.all().order_by("?")[:15]
    else:
        adaptations = []

    return render_to_response('index.html', locals(), RequestContext(request))

def browse(request):
    adaptations = Adaptation.objects.filter(visible=True).order_by("-id")
    paginator = Paginator(adaptations,25)

    page = request.GET.get('page')
    try:
        adaptations = paginator.page(page)
    except PageNotAnInteger:
        adaptations = paginator.page(1)
    except EmptyPage:
        adaptations = paginator.page(paginator.num_pages)

    return render_to_response('browse.html', locals(), RequestContext(request))

@staff_member_required
def evil_browse(request):
    adaptations = Adaptation.objects.filter(visible=False).order_by("-id")
    paginator = Paginator(adaptations,25)

    page = request.GET.get('page')
    try:
        adaptations = paginator.page(page)
    except PageNotAnInteger:
        adaptations = paginator.page(1)
    except EmptyPage:
        adaptations = paginator.page(paginator.num_pages)

    return render_to_response('browse.html', locals(), RequestContext(request))

def new_panel(request):
    pages = BarbiePage.objects.all()
    pages_json = json.dumps({ p.id: p.simple() for p in pages })

    random_page_id = random.choice(pages).id;

    prevent_uploads = PREVENT_UPLOADS
    imgur_client_id = IMGUR_CLIENT_ID

    return render_to_response('new_panel.html', locals(), RequestContext(request))

def save_page(request):
    data  = {"saved": "False", "msg": "bad arguments"}
    if 'page_id' in request.POST and 'new_text' in request.POST and 'imgur_id' in request.POST:
        page_id = int(request.POST['page_id'])
        new_text = request.POST['new_text']
        imgur_id = request.POST['imgur_id']

        if not PREVENT_UPLOADS:
            try:
                a = Adaptation()
                a.page = BarbiePage.objects.get(id=page_id)

                a.new_text = new_text
                a.imgur_id = imgur_id
                print "set a bunch of things"

                a.save()

                data = {"saved": True, "msg": a.id, "redirect": reverse('view_panel', args=[a.id]) }
            except ValueError, e:
                data = {"saved": False, "msg": "problem saving"}
                print "[--ERROR--] failed to save this Adaptation", page_id, new_text, imgur_id
                print e
        else:
            data = {"saved": False} 


    return HttpResponse(json.dumps(data), content_type='application/json')

def view_panel(request, id):
    panel = Adaptation.objects.get(id=id)

    # todo: get prev/next ids
    cursor = connection.cursor()
    cursor.execute("select id from cebarbie_adaptation where id < %s and visible = 1 order by id desc limit 1", (id,))
    row = cursor.fetchone()
    if row:
        prev = int(row[0])
    else:
        prev = id

    cursor.execute("select id from cebarbie_adaptation where id > %s and visible = 1 order by id asc limit 1", (id,))
    row = cursor.fetchone()
    if row:
        next = int(row[0])
    else: 
        next = id

    return render_to_response('view_panel.html', locals(), RequestContext(request))

@staff_member_required
def endorse(request):
    data = {}
    if 'adaptation_id' in request.POST and 'endorsement' in request.POST:
        adaptation_id = json.loads(request.POST['adaptation_id'])
        endorsement = json.loads(request.POST['endorsement'])

        a = Adaptation.objects.get(id=adaptation_id)
        a.endorsed = endorsement
        a.save()
        data = {"endorsed": endorsement, "adaptation_id": adaptation_id}

    return HttpResponse(json.dumps(data), content_type='application/json')

@staff_member_required
def delete(request):
    data = {}
    if 'adaptation_id' in request.POST:
        adaptation_id = json.loads(request.POST['adaptation_id'])

        a = Adaptation.objects.get(id=adaptation_id)
        a.delete()
        data = {"deleted": adaptation_id}

    return HttpResponse(json.dumps(data), content_type='application/json')

def flag(request):
    data = {}
    if 'adaptation_id' in request.POST:
        adaptation_id = json.loads(request.POST['adaptation_id'])

        a = Adaptation.objects.get(id=adaptation_id)
        a.flagged = True
        a.visible = False
        a.save()
        data = {"flagged": adaptation_id}

    return HttpResponse(json.dumps(data), content_type='application/json')