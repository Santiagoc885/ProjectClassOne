from django.urls import path
from .views.ideas import base
from .views import (
    ideas
)

app_name = 'ideas'

urlpatterns = [
    
    path('base/', base, name='base'),
    
    path('ideas/list/', ideas.IdeaListView. as_view(), name='list'),
    path('ideas/create/', ideas.IdeaCreateView.as_view(), name='create'),
    path('ideas/<int:pk>/update/', ideas.IdeaUpdateView.as_view(), name='ideas_update'),
    path('ideas/<int:pk>/delete/', ideas.IdeaDeleteView.as_view(), name='ideas_delete'),
    path('ideas/<int:pk>/detail', ideas.IdeaDetailView.as_view(), name='ideas_detail'),
]
