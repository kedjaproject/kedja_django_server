from rest_framework import serializers, viewsets

from walls import models


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WallRole
        fields = ('user', 'roles')


class WallSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = models.Wall
        fields = '__all__'


# ViewSets define the view behavior.
class WallViewSet(viewsets.ModelViewSet):
    queryset = models.Wall.objects.all()
    serializer_class = WallSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        roles = models.WallRole.objects.create(
            wall=instance,
            user=self.request.user,
        )
        roles.roles.set([models.WALL_ROLES.OWNER])
