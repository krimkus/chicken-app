from django.conf.urls import patterns, url, include

from rest_framework import routers

from data import api


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'groups', api.GroupViewSet)
router.register(r'types', api.CheckinTypeViewSet)
router.register(r'questions', api.CheckinQuestionViewSet)
router.register(r'answers', api.CheckinAnswerViewSet)
router.register(r'checkins', api.CheckinViewSet)
router.register(r'responses', api.CheckinQuestionResponseViewSet)
router.register(r'reminders', api.ReminderTypeViewSet)


urlpatterns = patterns('data.views',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
)
