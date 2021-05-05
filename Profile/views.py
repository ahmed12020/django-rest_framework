from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer, ProfileDetailSerializer, ProfileSerializerAPIViw
from .paginations import ProfileLimitPagination, ProfilePagePagination
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView , RetrieveUpdateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# from django.views.decorators.csrf import csrf_exempt


def profile_home(request):
    return render(request, 'Profile/home.html')


#list Api
class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'title', 'content', 'email']
    ordering_field = ['name']
    permission_classes = [IsAdminUser]
    pagination_class = ProfileLimitPagination


#dtail Api
class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer


#update Api
class ProfileUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


#delete Api
class ProfileDeleteAPIView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


#detail and update Api
class ProfileDetailUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


#create Api
class ProfileCreateApIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


#viewsets
class ProfielViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializers = ProfileSerializerAPIViw(profiles, many=True)
        return Response(serializers.data)














