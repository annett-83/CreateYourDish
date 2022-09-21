import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Dishes

# упрощеное описание сериалайзера для определенной модели
class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        #fields = ("title", "content", "cat")
        fields = "__all__"  # если хотим чтобы заполнялись все поля


# Разборочный материал
# class DishesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# class DishesSerializer(serializers.Serializer):  # сериализатор проверяет джайсон запрос
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)  # время создания записи не обязательное поле
#     time_update = serializers.DateTimeField(read_only=True)  # время изменения записине обязательное поле
#     is_published = serializers.BooleanField(default=True)  # опубликована или не опубликована автоматически
#     cat_id = serializers.IntegerField()  # ссылка на категорию
#
#     def create(self, validated_data): # создаем новые объекты а бд
#         return Dishes.objects.create(**validated_data) # словарь из проверенных данных прешедших с пост-запроса
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

# # преобоазование в джайсон строку
# def encode():  # преобразование информации в джайсон формат
#     model = DishesModel('xxx', 'Content: ooooo')
#     # пропускаем данный объект model через сериализатор
#     model_sr = DishesSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')  # выдает данные сериализованные в джайсон формат
#     # преобразование в байтовую джайсон строку передавакмую клиенту для дальнейшего парсинга
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# #преобразует джкйсон формат в строку
# def decode():
#     stream = io.BytesIO(b'{"title":"xxx", "content":"Content: ooooo "}')
#     data = JSONParser().parse(stream)
#     serializer = DishesSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
