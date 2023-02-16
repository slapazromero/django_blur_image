from django.urls import path
from blur_image.views import ImageCreateView, ImageDetailView, ImageListView, ImageUpdateView, ImageDeleteView, ImageView

urlpatterns = [
    path("", ImageView.as_view(), name="image_view"),
    path('album/', ImageListView.as_view(), name='image_list_view'),
    path('detail/<int:pk>', ImageDetailView.as_view(), name='image_detail_view'),
    path('create/', ImageCreateView.as_view(), name='image_create_view'),
    path('update/<int:pk>', ImageUpdateView.as_view(), name='image_update_view'),
    path('delete/<int:pk>', ImageDeleteView.as_view(), name='image_delete_view'),
    
]
