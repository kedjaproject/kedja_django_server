from rest_framework import serializers, viewsets, generics

from walls import models
from walls import permissions


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WallRole
        fields = ('user', 'roles')


class WallSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = models.Wall
        fields = '__all__'


class WallListView(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = models.Wall.objects.all()
    serializer_class = WallSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        roles = models.WallRole.objects.create(
            wall=instance,
            user=self.request.user,
        )
        roles.roles.set([models.WALL_ROLES.OWNER])


class WallDetailView(generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = models.Wall.objects.all()
    serializer_class = WallSerializer
    permission_classes = (permissions.ViewWall,)


class WallUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView, viewsets.GenericViewSet):
    queryset = models.Wall.objects.all()
    serializer_class = WallSerializer
    permission_classes = (permissions.ModifyWall,)
