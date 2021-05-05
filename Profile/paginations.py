from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ProfileLimitPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 5


class ProfilePagePagination(PageNumberPagination):
    page_size = 5