from django.test import TestCase
from events.models import Event, Subscription, StateChoices
from django.contrib.auth.models import User


class ModelEventTestClass(TestCase):
    """This test class is constructed to test the functionality of the Model Event.

    Implement in this class all additional tests for this model.
    Current tests:
        -Test comment <max_length> attr
        -Test comment <default_value> attr
        -Test description <max_length> attr
        -Test description <default_value> attr
        -Test state <max_length> attr
        -Test state <default_value> attr
    """

    @classmethod
    def setUpTestData(cls):
        """Class Method.

        This method is used only one time when the tests start.
        Create a new object User and Event to be used in this tests
        """

        print('Running unit tests for: MODELS')
        date = '2021-11-15 00:11:22'
        user = User.objects.create_user('john', 'john@email.com', 'JohnPassword')

        Event.objects.create(
                            author=user,
                            event_date=date
        )

    def test_title_label_max_length(self):
        """Test the max length attr of the field <title_text>"""

        max_length = Event._meta.get_field('title_text').max_length
        self.assertEqual(max_length, 36)

    def test_title_label_default_value(self):
        """Test the default value attr of the field <title_text>"""

        default_title = Event._meta.get_field('title_text').verbose_name
        self.assertEqual(default_title, 'Title')

    def test_description_label_max_length(self):
        """Test the max length attr of the field <description_text>"""

        max_length = Event._meta.get_field('description_text').max_length
        self.assertEqual(max_length, 300)

    def test_description_label_default_value(self):
        """Test the default value attr of the field <description_text>"""

        default_title = Event._meta.get_field('description_text').verbose_name
        self.assertEqual(default_title, 'Description')

    def test_state_label_max_length(self):
        """Test the max length attr of the field <state_type>"""

        max_length = Event._meta.get_field('state_type').max_length
        self.assertEqual(max_length, 36)

    def test_state_label_default_value(self):
        """Test the default value attr of the field <state_type>"""

        default_state = Event._meta.get_field('state_type').verbose_name
        self.assertEqual(default_state, StateChoices.DRAFT)


class ModelSubscriptionTestClass(TestCase):
    """This test class is constructed to test the functionality of the Model Event.

    Implement in this class all additional tests for this model.

    Current tests:
        -Test comment <max_length> attr
        -Test comment <default_value> attr
    """

    @classmethod
    def setUpTestData(cls):
        """Class Method.

        This method is used only one time when the tests start.
        Create a new object User, Event and Subscription to be used in this tests
        """
        date = '2021-11-15 00:11:22'
        user = User.objects.create_user('john', 'john@email.com', 'JohnPassword')
        Event.objects.create(
            author=user,
            event_date=date
        )

        Subscription.objects.create(
            username=user,
            event_sub=Event.objects.get(id=1)
        )

    def test_comment_label_max_length(self):
        """Test the max length attr of the field <comment>"""

        max_length = Subscription._meta.get_field('comment').max_length
        self.assertEqual(max_length, 300)

    def test_comment_label_default_value(self):
        """Test the default value attr of the field <comment>"""

        default_comment = Subscription._meta.get_field('comment').verbose_name
        self.assertEqual(default_comment, 'Default comment')
