from django.db import models
from enum import Enum
from django.contrib.auth.models import User


class StateChoices(Enum):
    """Represent the possibles state that an event can have.
    Draft = This events can't be seen.
    Private: This events can only be seen by log in users.
    Public: This events can be seen by all users.
    """
    DRAFT = 'DRAFT'
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'

    @classmethod
    def states(cls):
        return tuple((attr.name, attr.value) for attr in cls)


class Event(models.Model):
    """Create the representation for the Event entity.
    Author: The person who created the event.
    Title_text: The title of the event.
    Description_test: The description of the event.
    Event_date: The date when the event will star. Format: YYYY-MM-DD HH-MM-SS
    State_type: The current status of the event.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', default='')
    title_text = models.CharField('Title', max_length=36)
    description_text = models.CharField('Description', max_length=300)
    event_date = models.DateTimeField('Event date')
    state_type = models.CharField(StateChoices.DRAFT, max_length=36, choices=StateChoices.states())

    def __str__(self):
        return '{} {} {} {}'.format(self.id, User.username, self.title_text, self.state_type)


class Subscription(models.Model):
    """Create the representation for the Subscription entity.
    Username: The person who created the subscription.
    Event_sub: The event to which the subscription belongs.
    Comment: A comment from the user who subscribed to the event.
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default='')
    event_sub = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event', default='')
    comment = models.CharField('Default comment', max_length=300)

    def __str__(self):
        return '{} {} {}'.format(self.id, User.username, self.comment)
