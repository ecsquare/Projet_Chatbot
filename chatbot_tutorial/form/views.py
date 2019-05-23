from django.shortcuts import render
 
from .forms import FeedbackForm
 
 
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            
    else:
        form = FeedbackForm()
    return render(request, 'chatbot_tutorial/feed.html', {'form': form})
