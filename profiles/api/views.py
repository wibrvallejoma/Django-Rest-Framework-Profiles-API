from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import (ProfileSerializer,
                                      ProfileStatusSerializer,
                                      ProfileAvatarSerializer)
from profiles.api.permissions import IsOwnProfileReadOnly, IsOwnerOrReadOnly

# Custom viewset by rest_framework
class ProfileViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["city"]


# Filter status by parameter. Example.
# http://127.0.0.1:8000/api/status/?username=admin
class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)



# Viewset model by rest_framework
# class ProfileViewSet(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


# Generics
# class ProfileList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


# To update the Avatar image is better to use Generics instead of Viewset.
class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    # Override get object method
    def get_object(self):
        # Update only
        profile_object = self.request.user.profile
        return profile_object
