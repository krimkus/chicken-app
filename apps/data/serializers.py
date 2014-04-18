from django.contrib.auth.models import User, Group
from rest_framework import serializers

from data.models import CheckinType, CheckinQuestion, CheckinAnswer, Checkin, CheckinQuestionResponse, ReminderType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CheckinTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckinType
        fields = ('created_by', 'name', 'position')


class CheckinQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckinQuestion
        fields = ('checkintype',)


class CheckinAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckinAnswer
        fields = ('question',)


class CheckinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checkin
        fields = ('checkintype', 'created_by', 'created_at')


class CheckinQuestionResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckinQuestionResponse
        fields = ('checkin', 'question', 'value', 'created_by', 'created_at')
        read_only_fields = ('created_by',)


class ReminderTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReminderType
        fields = ('body', 'created_by', 'created_at')
        read_only_fields = ('created_by',)
