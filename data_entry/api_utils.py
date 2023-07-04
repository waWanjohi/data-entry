from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import BasicPagination, PaginationHandlerMixin


class APIList(APIView, PaginationHandlerMixin):
    """
    A custom implementation of the Django REST Framework's
    `APIView` class.

    It uses `PaginationHandlerMixin`, a custom pagination class

    Usage:

    `class MyModelList(APIList):`

        `model_class = MyModel`

        `serializer_class = MyModelSerializer`

    """

    permission_classes = [IsAuthenticated]
    pagination_class = BasicPagination
    serializer_class = None
    model_class = None

    def get_queryset(self, *args, **kwargs):
        """
        This method is used to get the queryset for the view.
        Will return only active objects from the logged-in user's region
        """
        return self.model_class.objects.all()

    # `get` method is provided by Django REST Framework and is a helper
    # method that determines what a get request will return
    def get(self, request, format=None, *args, **kwargs):
        results = self.get_queryset(*args, **kwargs).order_by("-id")

        page = self.paginate_queryset(results)

        if page is not None:
            response = self.get_paginated_response(
                self.serializer_class(page, many=True).data
            )
        else:
            #  TODO: Correct the instance of the serializer
            response = self.serializer_class(many=True).data  # noqa

        return Response(response.data, status=status.HTTP_200_OK)

    # `post` method is provided by Django REST Framework and is a helper
    # method that determines what a post request will return
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                if not serializer.instance:
                    serializer.validated_data["created_by"] = request.user
                serializer.save()

            except Exception as e:
                return Response(
                    {"message": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIDetail(APIView):
    """
    Shows a detailed view of the API object.

    It uses `PaginationHandlerMixin`, a custom pagination class.
    This can be much helpful in cases where you might need to do a query
    to get unique data for a particular model.

    Usage:
    class MyModelList(APIList):
        model_class = MyModel
        serializer_class = MyModelSerializer


    """

    permission_class = [IsAuthenticated]
    model_class = None
    serializer_class = None

    # `get_object` is provided by Django REST Framework and is a helper
    # method that fetches an object from the database.
    def get_object(self, pk):

        return get_object_or_404(self.model_class, pk=pk)

    # `get` method is provided by Django REST Framework and is a helper
    # method that determines what a get request will return
    def get(self, request, pk, format=None):
        try:
            object = self.get_object(pk)

            response = self.serializer_class(object).data
            return Response(response)
        except self.model_class.DoesNotExist:
            return Response(
                f"{self.model_class.__name__} does not exist",
                status=status.HTTP_404_NOT_FOUND,
            )

    # `put` method is provided by Django REST Framework and is a helper
    # method that determines what a put request will return
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = self.serializer_class(object, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)

        object.is_active = False

        object.save()
        return Response(
            {"message": f"{object.__str__()} has been deleted"},
            status=status.HTTP_301_MOVED_PERMANENTLY,
        )


@api_view(["POST"])
def filter_queryset(request, model, serializer):


    try:
        if request.data.created_at:
            query_set = model.objects.filter(
                created_at=request.data.date_created
            )
            serializer = serializer(query_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.data.name:
            query_set = model.objects.filter(name=request.data.name)
            serializer = serializer(query_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return f"An Error occurred: {e} "
