from django.test import TestCase
from events.models import Event, StateChoices
from django.urls import reverse
from django.contrib.auth.models import User


class EventListViewTest(TestCase):
    """This test class is constructed to test the functionality of the EventList view.

    Implement in this class all additional tests for this model.
    Current tests:
        -Test url location
        -Test view template
    """

    @classmethod
    def setUpTestData(cls):
        """Class Method.

        This method is used only one time when the tests start.
        """

        print('Running unit tests for: VIEWS')

    def test_url_location(self):
        """Test if the location of the EventList view is correct"""

        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """Test if the template used by the view EventList is correct"""

        response = self.client.get('/events/')
        self.assertTemplateUsed(response, 'events/index.html')


class EventSubscribedViewTests(TestCase):
    """This test class is constructed to test the functionality of the EventSubscribed view.

    Implement in this class all additional tests for this model.
    Current tests:
        -Test url location
        -Test view template
    """

    @classmethod
    def setUpTestData(cls):
        """Class Method.

        This method is used only one time when the tests start.
        Create a User and Event objects to be used in this tests.
        """

        user = User.objects.create_user('Manuel', 'manuel@email.com', 'manuelpassword')
        user.save()
        Event.objects.create(
            author=user,
            title_text='New event',
            description_text='An incredible description',
            event_date='2021-11-15 00:11:22',
            state_type=StateChoices.DRAFT
        )

    def test_url_location(self):
        """Test if the location of the EventSubscribed view is correct"""

        response = self.client.get(reverse('event', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """Test if the template used by the view EventList is correct"""

        response = self.client.get(reverse('event', args=[1]))
        self.assertTemplateUsed(response, 'events/event.html')


class EventPostViewTests(TestCase):
    """This test class is constructed to test the functionality of the EventPost view.

    Implement in this class all additional tests for this model.
    Current tests:
        -Test url location
        -Test view template
    """

    @classmethod
    def setUpTestData(cls):
        """Class Method.

        This method is used only one time when the tests start.
        Create a User and Event objects to be used in this tests.
        """

        user = User.objects.create_user('Manuel', 'manuel@email.com', 'manuelpassword')
        user.save()
        Event.objects.create(
            author=user,
            title_text='New event',
            description_text='An incredible description',
            event_date='2021-11-15 00:11:22',
            state_type=StateChoices.DRAFT
        )

    def test_url_location(self):
        """Test if the location for the EvenPost view is correct"""

        # We must login to access this view.
        self.client.login(username='Manuel', password='manuelpassword')

        response = self.client.get('/events/post/')
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """Test if the template used by the view EventPost is correct"""

        # We must login to access this view.
        self.client.login(username='Manuel', password='manuelpassword')

        response = self.client.get('/events/post/')
        self.assertTemplateUsed(response, 'events/event_create.html')


class SignUpViewTests(TestCase):
    """This test class is constructed to test the functionality of the SignUp view.

    Implement in this class all additional tests for this model.
    Current tests:
        -Test url location
        -Test view template
    """

    @classmethod
    def setUpTestData(cls):
        """Class Method.

        This method is used only one time when the tests start.
        """
        pass

    def test_url_location(self):
        """Test if the location for the SignUp view is correct"""

        response = self.client.get('/events/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """Test if the template used by the view SignUp is correct"""

        response = self.client.get('/events/signup/')
        self.assertTemplateUsed(response, 'events/signup.html')
