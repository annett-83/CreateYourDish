from _testcapi import raise_exception
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dishes, Category
from .serializers import DishesSerializer

# опримизация данных в классах с помощью model Viewset!!!!!
class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer

    #прописываен с помощью декоратора новый маршрут получаем категории
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})



# #обработчик гет и пост запросав класс
# class DishesAPIList(generics.ListCreateAPIView):
#     queryset = Dishes.objects.all()
#     serializer_class = DishesSerializer
#
# # это только апдэйт
# # class DishesAPIUpdate(generics.UpdateAPIView):
# #     queryset = Dishes.objects.all() #ленивый запрос, будет обновляться только то, что было измениною
# #     serializer_class = DishesSerializer
#
#
# #     можно объеденить и делти и апдайт и запросить
# class DishesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Dishes.objects.all()
#     serializer_class = DishesSerializer

# # через сериалайзер превращаем в джейсон строку через функции
# class DishesAPIView(APIView):
#     def get(self, request):
#         d = Dishes.objects.all() # запрашивает все из базы данных
#         return Response({'posts': DishesSerializer(d, many=True).data})

    # #обработчик гет и пост запросав через функции
    # def post(self, request):
    #     serializer = DishesSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     # позволяет добовлять новые записи в бвзу данных
    #     serializer.save() #вызовет метод креэйт из сериализатора
    #
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None) # проверяет значения ключа в юрл запросе в бд
    #     if not pk:
    #         return Response({"error": "Method PUT not allowed"}) # сообщаем клиенту что запрос пут(изменения в записи ) не может быть выполнен
    #
    #     try:
    #         instance = Dishes.objects.get(pk=pk)
    #
    #     except:
    #         return Response({"error": "Object does not exists"})
    #     # если ключ совпал пропускаем через сериалайзер
    #     serializer = DishesSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception==True)
    #     serializer.save() # вызывает метод апдэйт, так как указаны два параметра data? instance
    #     return Response({"post": serializer.data})
    #
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method PUT not allowed"})
    #     try:
    #         instance = Dishes.objects.get(pk=pk)
    #
    #     except:
    #         return Response({"error": "Object does not exists"})
    #     serializer = DishesSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception == True)
    #     serializer.save()  # вызывает метод апдэйт, так как указаны два параметра data? instance
    #     return Response({"post": serializer.data})



# class DishesAPIView(generics.ListAPIView):
#     queryset = Dishes.objects.all()
#     serializer_class = DishesSerializer
