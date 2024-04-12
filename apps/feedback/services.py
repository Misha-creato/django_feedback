from feedback.models import Feedback


def create_feedback_object(data):
    Feedback.objects.create(
        title=data['title'],
        text=data['text'],
        full_name=data['full_name'],
        contacts=data['contacts'],
    )
