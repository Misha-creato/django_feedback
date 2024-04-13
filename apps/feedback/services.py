from django.http import QueryDict
from django.db import DatabaseError

from feedback.models import Feedback


def create_feedback_object(data: QueryDict):
    try:
        Feedback.objects.create(
            title=data['title'],
            text=data['text'],
            full_name=data['full_name'],
            contacts=data['contacts'],
        )
    except DatabaseError as ex:
        print(f'Ошибка базы данных {ex}')
