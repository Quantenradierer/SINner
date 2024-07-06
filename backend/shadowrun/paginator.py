from rest_framework import pagination
from rest_framework.response import Response


class Paginator(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    max_page_size = 1000
    page_query_param = "page"

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.page.next_page_number() if self.page.has_next() else None,
                "previous": (
                    self.page.previous_page_number()
                    if self.page.has_previous()
                    else None
                ),
                "number": self.page.number + 1,
                "count": self.page.paginator.count,
                "results": data,
            }
        )
