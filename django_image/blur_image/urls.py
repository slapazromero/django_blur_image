from django.urls import path
from blur_image.views import ImageCreateView, ImageDetailView, ImageListView, ImageDeleteView, ImageView, ImageBlurView, detect_faces, blur_image

urlpatterns = [
    path("", ImageView.as_view(), name="image_view"),
    path('album/', ImageListView.as_view(), name='image_list_view'),
    path('detail/<int:pk>', ImageDetailView.as_view(), name='image_detail_view'),
    path('create/', ImageCreateView.as_view(), name='image_create_view'),
    path('delete/<int:pk>', ImageDeleteView.as_view(), name='image_delete_view'),
    path('blur/<int:pk>', ImageBlurView.as_view(), name = 'image_blur_view'),
    path('amazon_face/<int:pk>', detect_faces, name = 'detect_faces'),
    path('blur_image/<int:pk>', blur_image, name='blur_image'),
    
]
