from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from data.serializers import *

# from data.models import CheckinType, CheckinQuestion, CheckinAnswer, Checkin


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class CreatorCanEditPermission(SafeMethodsOnlyPermission):
    """Allow everyone to list or view, but only the other can modify existing instances"""
    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            # Either a list or a create, so no author
            can_edit = True
        else:
            can_edit = request.user == obj.created_by
        return can_edit or super(CreatorCanEditPermission, self).has_object_permission(request, view, obj)


class LimitToCreatorViewSet(viewsets.ModelViewSet):
    permission_classes = [
        CreatorCanEditPermission
    ]


class UserViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CheckinTypeViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows checkin types to be viewed or edited.
    """
    queryset = CheckinType.objects.all()
    serializer_class = CheckinTypeSerializer


class CheckinQuestionViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = CheckinQuestion.objects.all()
    serializer_class = CheckinQuestionSerializer


class CheckinAnswerViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows answers to be viewed or edited.
    """
    queryset = CheckinAnswer.objects.all()
    serializer_class = CheckinAnswerSerializer


class CheckinViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows checkins to be viewed or edited.
    """
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer


class CheckinQuestionResponseViewSet(LimitToCreatorViewSet):
    """
    API endpoint that allows checkin responses to be viewed or edited.
    """
    queryset = CheckinQuestionResponse.objects.all()
    serializer_class = CheckinQuestionResponseSerializer
