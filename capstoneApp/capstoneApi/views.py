from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_overview(request):
    data = {
        "all_entries":"getItems/",
        "single_entry": "getItem/<str:pk>/",
        "create_entry": "insertItem/",
        "update_entry": "updateItem/<str:pk>/",
        "delete_entry": "deleteItem/<str:pk>/",
    }
    return Response(data=data, status=status.HTTP_200_OK)
    
# @api_view(['GET'])
# def get_items(request):
#     try:
#         entries = Moisture.objects.all()
#         serializer = MoistureSerializer(entries, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     except Moisture.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def get_item(request, pk):
#     try:
#         entry = Moisture.objects.get(id=pk)
#         serializer = MoistureSerializer(entry)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Moisture.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def insert_item(request):
#     print(request.data)
#     serializer = MoistureSerializer(data=request.data)

#     if serializer.is_valid(): 
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['PUT'])
# def update_item(request, pk):
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
# def delete_item(request, pk):
#     try:
#         entry = Moisture.objects.get(id=pk)
#         entry.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
