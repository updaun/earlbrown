from django.shortcuts import render
from rest_framework import generics

from .models import Menu
from .serializers import MenuSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MenuCreateAPI(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailAPI(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_object(self, pk):
        return Menu.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        Menu = self.get_object(pk)
        serializer = self.get_serializer(Menu)
        return Response(serializer.data)


class MenuUpdateAPI(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class MenuDeleteAPI(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_object(self, pk):
        return Menu.objects.get(pk=pk)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
