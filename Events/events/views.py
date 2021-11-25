from django.shortcuts import render
from .models import Event, Subscription
from django.views import View
from django.contrib.auth import authenticate, login, logout
from itertools import chain
from .forms import NewEventForm, SubscriptionForm, SignUpForm
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User


class EventList(View):
    """Create the view that show the public and private events.
    If the user is log in, the view will return public and private events.
    If the user is log out, the view will return only the public events.
    This view also implement the log in for the users.
    """

    template = ''

    def get(self, request):
        """This method will be used when the view receive a GET request"""

        return render(request, self.template, self.get_context(request))

    def post(self, request):
        """This method will be used when the view receive a POST request
        Allow user to log in
        """

        if 'logout' in request.POST:
            logout(request)

        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

        return render(request, self.template, self.get_context(request))

    def get_context(self, request):
        """Create the context for the template.
        Depend if the user is log in or log out, the context will change.
        """

        if request.user.is_authenticated:
            public = Event.objects.filter(state_type='PUBLIC')
            private = Event.objects.filter(state_type='PRIVATE')
            event_list = list(chain(public, private))

            context = {
                'event_list': event_list,
                'login': request.user.username,
            }
        else:
            event_list = Event.objects.filter(state_type='PUBLIC')

            context = {
                'event_list': event_list,
            }

        return context


class EventSubscribed(View):
    """Create the view that allow a log in User to subscribed to an event.
    This view populate the template with a form and then process it to get
    the comment.
    The User data is obtained by the request.
    """
    template = ''

    def get(self, request, event_id):
        """This method will be used when the view receive a GET request.
        If the requested Event does not exist the view will return a 404.
        If the user is no authenticated, the form will not be pass to the context.
        """
        form_subscribed = SubscriptionForm()

        try:

            event = Event.objects.filter(id=event_id)
            username = event[0].author.username

            if request.user.is_authenticated:

                context = {
                    'event': event,
                    'username': username,
                    'form_subscribed': form_subscribed,
                    'login': True
                }

            else:

                context = {
                    'username': username,
                    'event': event,
                    'login': False
                }

        except ValueError:
            raise Http404('Event does not exist')

        return render(request, self.template, context)

    def post(self, request, event_id):
        """This method will be used when the view receive a POST request
        Allow users to subscribed to an event.
        """
        subscribed_form = SubscriptionForm(request.POST)

        if subscribed_form.is_valid() and request.user.is_authenticated:

            user_subscription = Subscription()
            user_subscription.event_sub = Event.objects.filter(id=event_id)[0]
            user_subscription.username = request.user
            user_subscription.comment = subscribed_form.cleaned_data['comment']
            user_subscription.save()

        return HttpResponseRedirect('/events/')


class EventPost(View):
    """Create the view that allow for a User to Post a new Event.
    If the User is not Authenticated it will return a PermissionDenied.
    If the User is Authenticated it will return a the template populated by
    a NewEventForm.
    """
    template = ''

    def get(self, request):
        """This method will be used when the view receive a GET request.
        If the user is not authenticated Event the view will return a PermissionDenied.
        If the user is authenticated it will render the template.
        """
        if request.user.is_authenticated:
            form = NewEventForm()

            context = {
                'form': form
            }

            return render(request, self.template, context)

        else:

            return PermissionDenied()

    def post(self, request):
        """This method will be used when the view receive a POST request.
        Process the NewEventForm and create a new Event which will be saved
        in the database.
        """

        event_form = NewEventForm(request.POST)

        if event_form.is_valid() and request.user.is_authenticated:

            new_event = Event()

            new_event.title_text = event_form.cleaned_data['title']
            new_event.event_date = event_form.cleaned_data['date']
            new_event.state_type = event_form.cleaned_data['state']
            new_event.description_text = event_form.cleaned_data['description']
            new_event.author = request.user

            new_event.save()

            return HttpResponseRedirect('/events/')

        else:

            return HttpResponseRedirect('/events/post/')


class SignUp(View):
    """Create the view that allow a user to Sign up.
    This view populate the template with a form and then process it in the post request.
    """
    template_name = ''

    def get(self, request):
        """This method will be used when the view receive a GET request.
        Create the context that the template will received.
        """
        form = SignUpForm()

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        """This method will be used when the view receive a POST request
        Process a SignUpForm to create a new user.
        """
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():

            user = User.objects.create_user(
                username=signup_form.cleaned_data['username'],
                password=signup_form.cleaned_data['password'],
                email=signup_form.cleaned_data['email'],
                first_name=signup_form.cleaned_data['first_name'],
                last_name=signup_form.cleaned_data['last_name']
            )

            user.save()

            return HttpResponseRedirect('/events/')

        else:

            return Http404('Passwords does not much')
