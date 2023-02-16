from django.urls import resolve, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from blur_image.models import Image
from blur_image.forms import ImageForm

# Create your views here.
class ImageView(TemplateView):
    template_name = "blur_image/image_view.html"


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('image-list-view')
    
class ImageListView(ListView):
    model = Image
    
class ImageDetailView(DetailView):
    model = Image
    
class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('image-list-view')
    
class ImageDeleteView(DeleteView):
    pk_url_kwarg = 'pk'
    model = Image
    success_url = '/images/album'

