from rest_framework import status
from rest_framework.response import Response


class TableView:
    def __init__(self, queryset, serializer_class):
        self.queryset = queryset
        self.serializer_class = serializer_class

    def get_table_data(self):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
