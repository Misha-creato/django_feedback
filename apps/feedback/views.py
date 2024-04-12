from django.shortcuts import render, redirect
from django.views import View
from feedback.models import Feedback


class CreateFeedback(View):
    model = Feedback

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='send_feedback.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        self.model.objects.create(
            title=data['title'],
            text=data['text'],
            full_name=data['full_name'],
            contacts=data['contacts'],
        )
        return redirect('feedback_answer')


def feedback_answer_view(request):
    return render(request=request, template_name='feedback_answer.html')
