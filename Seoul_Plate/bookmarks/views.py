from django.db.models import F
from rest_framework import status, mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from bookmarks.serializers import BookMarkSerializer
from restaurant.models import Restaurant
from .models import BookMark
from .permissions import IsOwnerOrReadOnly


class BookMarkViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Race Condition 방지 코드 필요
        # https://docs.djangoproject.com/en/3.0/ref/models/expressions/#avoiding-race-conditions-using-f
        # https://docs.djangoproject.com/en/3.0/ref/models/expressions/#f-expressions
        # ex) Restaurant.objects.filter(id=self.request.data['restaurant']).update(rest_count=F('rest_count') + 1)
        # 여기 코드가 있으면 admin 에서는 작동 하지 않으므로 model.save() override 하는게 좋음
        serializer.save(
            bookmark_user=self.request.user,
        )
