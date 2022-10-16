from django.shortcuts import render
from rest_framework import generics
from .models import Menu, MenuImage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .utils import get_menu_info


class MenuCreateView(APIView):
    def get(self, request):
        return render(request, "menu/create.html", {})


class MenuListView(APIView):
    def get(self, request):
        menu_list = Menu.objects.all()
        return render(request, "menu/list.html", {"menu_list": menu_list})


class MenuDetailView(APIView):
    def get(self, request, pk):
        menu_info = get_menu_info(request, pk)
        return render(request, "menu/detail.html", menu_info)


class MenuUpdateView(APIView):
    def get(self, request, pk):
        menu_info = get_menu_info(request, pk)
        return render(request, "menu/update.html", menu_info)
