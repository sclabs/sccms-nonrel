from models import Comic
from django.shortcuts import render_to_response, redirect, get_object_or_404
from comicms.settings import SITE_TITLE
import random
from filetransfers.api import serve_file

def lastcomic(request):
    comic = Comic.objects.order_by('-number')[0]
    sitetitle = SITE_TITLE
    return render_to_response('comic.html', locals())

def randomcomic(request):
    latestcomic = Comic.objects.order_by('-number')[0]
    randomnumber = random.randint(1, latestcomic.number)
    return redirect('particular', unicode(randomnumber))

def particularcomic(request, number):
    comic = Comic.objects.get(number=int(number))
    sitetitle = SITE_TITLE
    return render_to_response('comic.html', locals())

def previouscomic(request, number):
    if number == u'1':
        return redirect('particular', u'1')
    return redirect('particular', unicode(int(number) - 1))

def nextcomic(request, number):
    if number == unicode(Comic.objects.order_by('-number')[0].number):
        return redirect('particular', unicode(Comic.objects.order_by('-number')[0].number))
    return redirect('particular', unicode(int(number) + 1))

def get_comic(request, filename):
    comic = get_object_or_404(Comic, filename=filename)
    return serve_file(request, comic.img_src)
