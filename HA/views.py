# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from connection import connect
# from bson.json_util import dumps
import json
# Create your views here.

@api_view(['GET', 'POST'])
def academic_histories(request):
    db = connect("AHistory")

    items = [x for x in db.find({},{'_id' : 0})] 
    if request.method == 'GET':
        return Response(items)
    elif request.method == 'POST':
        try:
            db.insert_one(request.data)
            if 'id' in request.data.keys():
                return Response({'error':'id already created'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({'error':'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'PUT', 'DELETE'])
def academic_history(request, id):
    db = connect("AHistory")
    print(id)
    item = list(db.find({'id' : id},{'_id':0}))
    if request.method == 'GET':
        if len(item) == 0:
            return Response({'error':'element missing'}, status=status.HTTP_404_NOT_FOUND)
        return Response(item[0])
    elif request.method == 'PUT':
        try:
            db.update_one({'id':id}, {'$set': request.data})
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'error':'Failed to update'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        try:
            db.delete_one({'id':id})
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error':'Failed to delete'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)