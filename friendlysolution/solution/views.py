
from tkinter import Image

from .serializers import ImageInfoSerializer

from rest_framework import viewsets
from .models import ImageInfoo
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageInfoSerializer
    queryset = ImageInfoo.objects.all()
    a = not None
    def get_queryset(self):
        image_queryset = ImageInfoo.objects.all()
        return image_queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance=instance)
        return Response("Deleted successful")
    