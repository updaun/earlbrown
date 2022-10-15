from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MenuCreateView(APIView):
    def get(self, request):
        return render(request, "menu/create.html", {})


class MenuListView(APIView):
    def get(self, request):
        menu_list = Menu.objects.all()
        return render(request, "menu/list.html", {"menu_list": menu_list})


class MenuDetailView(APIView):
    def get(self, request, pk):
        menu = Menu.objects.filter(id=pk).first()
        return render(request, "menu/detail.html", {"menu": menu})


class MenuUpdateView(APIView):
    def get(self, request, pk):
        menu = Menu.objects.filter(id=pk).first()
        return render(request, "menu/update.html", {"menu": menu})
