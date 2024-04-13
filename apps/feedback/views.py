from django.shortcuts import render, redirect
from django.views import View

from feedback.services import create_feedback_object


class CreateFeedback(View):

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='send_feedback.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        create_feedback_object(data=data)

        return redirect('feedback_answer')


def feedback_answer_view(request):
    return render(request=request, template_name='feedback_answer.html')
