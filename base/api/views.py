from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET', 'PUT', 'POST'])
def get_routes(request):
    routes = [
        'GET /',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return Response(routes)

# Only allow get request using decorator.
@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    # Objects can not be passed in Response as it is. We need to convert it into JSON first.
    # Hence, we need serializers. Many represents are there many objects that we need to serialize and in this case,
    # we are having multiple objects.
    serializer = RoomSerializer(rooms, many = True)
    # return Response(rooms)
    return Response(serializer.data)

@api_view(['GET'])
def get_room(request,pk):
    room = Room.objects.get(id = pk)
    serializer = RoomSerializer(room, many = False)
    return Response(serializer.data)