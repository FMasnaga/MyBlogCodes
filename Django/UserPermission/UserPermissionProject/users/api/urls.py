from django.urls import path
from users.api.views import ProfileListView, ProfileDetailView

urlpatterns =[
    path ("profile/", ProfileListView.as_view(), name = "profile-list"),
    path ("profile/<int:pk>", ProfileDetailView.as_view(), name= "profile-detail")
]