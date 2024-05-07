from django.urls import path
from posts.views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:id>/', PostDetail.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('<int:id>/delete/', PostDelete.as_view(), name='post-delete')
]