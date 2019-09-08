from rest_framework import generics
from rest_framework import permissions

from users.api.serializers import ProfileSerializer
from users.api.permissions import isProfileOwnerOrReadOnly
from users.models import Profile

class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [isProfileOwnerOrReadOnly]

