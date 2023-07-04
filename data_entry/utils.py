from rest_framework.pagination import PageNumberPagination


class PaginationHandlerMixin(object):
    """
    This is a custom mixin to help paginate by a given number of items.
    It will be used together with the BasicPagination, and LargeSizePagination class,
    which is a custom implementation of the `PageNumberPagination` class.
    """

    @property
    def paginator(self):
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class BasicPagination(PageNumberPagination):
    """
    BasicPagination is a custom implementation of the `PageNumberPagination` class.
    It will be used together with the PaginationHandlerMixin class."""

    page_size = 40
    page_size_query_param = "limit"
    max_page_size = 1000


class LargeSizePagination(PageNumberPagination):
    """
    LargeSizePagination is a custom implementation of the `PageNumberPagination` class.
    It will be used together with the PaginationHandlerMixin class."""

    page_size = 100
    page_size_query_param = "limit"
    max_page_size = 10000
