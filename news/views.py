from django.shortcuts import render

# Create your views here.
from .utils import ndtv_page, cnn_page, zee_page


def headnews(request):
    story_list = ndtv_page()
    context = {
        "story_list": story_list
    }
    return render(request, 'news/head_lines.html', context)


def cnnheadlinenews(request):
    story_list = cnn_page()
    context = {
        "story_list": story_list
    }
    return render(request, 'news/head_lines.html', context)


def zeeheadlinenewes(request):
    story_list = zee_page()
    context = {
        "story_list": story_list
    }
    return render(request, 'news/head_lines.html', context)
