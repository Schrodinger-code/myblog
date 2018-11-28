from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import BlogType, Blog

# Create your views here.

def blog_list(request):
    return HttpResponse("hello World!")