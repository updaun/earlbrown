import os
from uuid import uuid4
from django.shortcuts import render
from rest_framework import generics
from earlbrown.settings import MEDIA_ROOT

from .models import Menu, MenuImage
from .serializers import MenuSerializer
from .serializers import MenuImageSerializer

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


# 프로필 이미지 업로드 API
class MenuImageCreateAPI(APIView):
    def post(self, request, pk):
        if request.FILES.get("file") is not None:
            file = request.FILES["file"]
            file_name = file.name
            extension = os.path.splitext(file_name)[1]
            uuid_name = uuid4().hex + extension

            dir_name = "menu"
            dir_path = os.path.join(MEDIA_ROOT, dir_name)

            # 폴더 생성 예외처리
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            save_path = os.path.join(dir_path, uuid_name)

            # 이미지 저장
            with open(save_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            menu_image_name = os.path.join(dir_name, uuid_name)

            menu_image = MenuImage(menu_id=pk, image=menu_image_name)

            menu_image.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_200_OK)
