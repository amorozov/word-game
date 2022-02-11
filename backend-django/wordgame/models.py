from django.db import models
from django_fsm import FSMField, transition

# Create your models here.
class Game(models.Model):
    class State(object):
        NEW = "NEW"
        QUESTIONED = "QUESTIONED"
        ANSWER_CORRECT = "ANSWER_CORRECT"
        ANSWER_INCORRENT = "ANSWER_INCORRECT"
        _EXPLAIN = "ANSWER_EXPLAIN"

    state = FSMField(default='new', protected = True)
