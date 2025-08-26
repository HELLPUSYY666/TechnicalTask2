from rest_framework.views import APIView
from shared.tools import TableView

from .models import Product
from .serializers import ProductTableSerializer


class TableAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        table_view = TableView(queryset, ProductTableSerializer)
        return table_view.get_table_data()
