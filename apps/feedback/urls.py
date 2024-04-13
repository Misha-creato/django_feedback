from django.urls import path
from feedback.views import (
    CreateFeedback,
    feedback_answer_view,
)


urlpatterns = [
    path(
        'send/',
        CreateFeedback.as_view(),
        name='send_feedback'
    ),
    path(
        'answer/',
        feedback_answer_view,
        name='feedback_answer'
    )
]
