from rest_framework import generics
from rest_framework import permissions

from rest_framework.viewsets import ModelViewSet
from vr.api.serializers import ProfileSerializer
from vr.api.permissions import isProfileOwnerOrReadOnly
from vr.models import Profile
#from rest_framework.viewsets import ReadOnlyModelViewSet

# class ProfileViewSet (ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet (ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, isProfileOwnerOrReadOnly]



# class ProfileListView(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [isProfileOwnerOrReadOnly]