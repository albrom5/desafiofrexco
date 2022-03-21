from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from rest_framework_csv import renderers

from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin

from desafioFrexco.core.models import User
from desafioFrexco.core.serializers import UserListSerializer, UserCreateSerializer


class CustomCSVRenderer(renderers.CSVRenderer):
    header = ['id', 'username', 'birth_date']


@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes((CustomCSVRenderer,))
def users_list_csv(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes((XLSXRenderer,))
def users_list_xlsx(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data)


class UsersListXLSX(XLSXFileMixin, ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'users.xlsx'


@api_view(['POST'])
def user_create(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)