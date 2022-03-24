from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import CommentsViewSet, FollowsViewSet, GroupViewSet
from .views import PostsViewSet

API_VERSION = 'v1/'
router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet, basename='api_posts')
router.register(r'follow', FollowsViewSet, basename='api_follow')
router.register(r'groups', GroupViewSet, basename='api_group')
router.register(
    r'posts/(?P<post_id>\d+)\/comments',
    CommentsViewSet,
    basename='api_comments'
)

urlpatterns = [
    path(API_VERSION, include(router.urls)),
    path(API_VERSION, include('djoser.urls')),
    path(API_VERSION, include('djoser.urls.jwt')),
    path(
        API_VERSION + 'api-token-auth/',
        views.obtain_auth_token,
        name='api_token'
    )

]
