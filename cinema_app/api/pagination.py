from rest_framework.pagination import CursorPagination

class RoomCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'number'