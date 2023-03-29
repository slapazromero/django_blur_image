from django.urls import resolve, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, TemplateView
from django.http import HttpResponse
from blur_image.models import Image
from blur_image.forms import ImageForm
from blur_image.utils import aws, blur
from django.http import JsonResponse
import json, os
from PIL import ImageFilter
from PIL import Image as PilImage

# Create your views here.
class ImageView(TemplateView):
    template_name = "blur_image/image_view.html"


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('image_list_view')
    
class ImageListView(ListView):
    model = Image
    
class ImageDetailView(DetailView):
    pk_url_kwarg = 'pk'
    model = Image
    
class ImageDeleteView(DeleteView):
    pk_url_kwarg = 'pk'
    model = Image
    success_url = reverse_lazy('image_list_view')
    
class ImageBlurView(DetailView):
    pk_url_kwarg = 'pk'
    model = Image
    template_name = 'blur_image/image_blur.html'


def detect_faces(request, pk):
    info = Image.objects.get(id = pk)
    file = str(info.image)
    name_file = info.name_image
    return aws(file, name_file)
    

def blur_image(request, pk):
    info = Image.objects.get(id = pk)
    file = str(info.image)
    path = file
    path = path.replace('media/', '')
    img = PilImage.open(file)
    body = json.loads(request.body)
    new_size = body.get('size')
    old_size = img.size
    img = img.resize((new_size[0], new_size[1]))
    

    coords = body.get('coords')
    for coord in coords:
        x = int(coord['x'])
        y = int(coord['y'])
        w = int(coord['w'])
        h = int(coord['h'])
        region = img.crop((x, y, x + w, y + h))
        for i in range(0, 40):
            region = region.filter(ImageFilter.BLUR)
        img.paste(region, (x, y, x + w, y + h))
    extension = os.path.splitext(path)
    path = 'media/' + extension[0] + "-blured" + extension[1]
    img = img.resize(old_size)
    img.save(path)
    
    image = Image(name_image=f'{info.name_image}_blured', image = path, is_blur = True)
    image.save()

    return JsonResponse({})
