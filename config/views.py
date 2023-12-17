from django.shortcuts import render
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request):
        return render(request, "index.html", {})


class AboutView(APIView):
    def get(self, request):
        return render(request, "about.html", {})
