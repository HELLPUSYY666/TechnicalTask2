from rest_framework.views import APIView
from shared.tools import TableView

from .models import User
from .serializers import UserTableSerializer


class TableAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        table_view = TableView(queryset, UserTableSerializer)
        return table_view.get_table_data()
