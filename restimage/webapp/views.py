from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer  

# Create your views here.

import tensorflow as tf
import sys
import os
# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#image_path = '..\..\media\p1.jpg'
image_path = 'http://127.0.0.1:8000/media/p3.jpg'

#image_data = tf.gfile.FastGFile(image_path, 'rb').read()

class StockList(APIView):

	def get(self,request):
		stocks = Stock.objects.all() 
		serializer = StockSerializer(stocks, many = True)
		return Response(serializer.data)

		

	def post(self,request):
		serializer = StockSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		

