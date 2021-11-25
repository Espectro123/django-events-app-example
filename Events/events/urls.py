from django.urls import path
from events.views import EventList, EventPost, EventSubscribed, SignUp


urlpatterns = [
    # /events/
    path('', EventList.as_view(template='events/index.html')),

    # /events/id/
    path('<int:event_id>/', EventSubscribed.as_view(template='events/event.html'), name='event'),

    # /events/post/
    path('post/', EventPost.as_view(template='events/event_create.html')),

    # /events/signup
    path('signup/', SignUp.as_view(template_name='events/signup.html')),
]