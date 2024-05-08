from django.urls import path
from posts.views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:id>/', PostDelete.as_view(), name='post-delete')
]