from django.shortcuts import render
from django.views import View

from feedback.models import Feedback


class Index(View):
    def get(self, request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        context = {
            'feedbacks': feedbacks,
        }
        return render(request=request, template_name='index.html', context=context)
