from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from firebase import getLights, getLight, insertLight

@api_view(['GET'])
def api_overview(request):
    data = {
        "all_entries":"getLights/",
        "single_entry": "getLight/<str:pk>/",
        "create_entry": "insertLight/",
        # "update_entry": "updateLight/<str:pk>/",
        # "delete_entry": "deleteLight/<str:pk>/",
    }
    return Response(data=data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_lights(request):
    try:
        entries = getLights()
        return Response(data=entries, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_light(request, pk):
    try:
        entry = getLight(pk)
        return Response(data=entry, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def insert_light(request):
    # serializer = MoistureSerializer(data=request.data)
    try:
        entry = insertLight(request.data)
        return Response(data=entry, status=status.HTTP_201_CREATED)
    except:  
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['PUT'])
# def update_light(request, pk):
#     try: 
#         entry = Moisture.objects.get(id=pk)
#         serializer = MoistureSerializer(instance=entry, data=request.data)

#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except: 
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['DELETE'])
# def delete_light(request, pk):
#     try:
#         entry = Moisture.objects.get(id=pk)
#         entry.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
