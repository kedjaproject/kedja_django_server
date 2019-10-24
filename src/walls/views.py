from rest_framework import serializers, viewsets

from walls.models import Wall, WallRole


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = WallRole
        fields = ('user', 'roles')


class WallSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Wall
        fields = '__all__'


# ViewSets define the view behavior.
class WallViewSet(viewsets.ModelViewSet):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer
