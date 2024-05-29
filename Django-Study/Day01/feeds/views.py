from django.shortcuts import render
from django.http import HttpResponse


def show_feed(reqeust):
    return HttpResponse("show feed")

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f"feed_id : {feed_id}, feed_content:{feed_content}")

def all_feed(request):
    return HttpResponse("all feed")
