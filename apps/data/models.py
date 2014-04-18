from django.db import models

import basic_models


class CheckinType(basic_models.SlugModel):
    position = models.IntegerField(default=0)


class CheckinQuestion(basic_models.DefaultModel):
    checkintype = models.ForeignKey(CheckinType)
    body = models.TextField()


class CheckinAnswer(basic_models.DefaultModel):
    question = models.ForeignKey(CheckinQuestion)
    body = models.TextField()


class Checkin(basic_models.DefaultModel):
    checkintype = models.ForeignKey(CheckinType)


class CheckinQuestionResponse(basic_models.DefaultModel):
    checkin = models.ForeignKey(Checkin)
    question = models.ForeignKey(CheckinQuestion)
    value = models.CharField(max_length=1024, blank=True)


class ReminderType(basic_models.SlugModel):
    position = models.IntegerField(default=0)
    body = models.TextField()
