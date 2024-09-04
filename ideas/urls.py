from django.urls import path
# from .views.ideas import base
from .views.ideas import list_ideas, create_idea, update_idea, delete_idea

app_name = 'ideas'

urlpatterns = [

    path('list/', list_ideas, name='list'),
    path('create/', create_idea, name='create'),
    path('update/<int:pk>/', update_idea, name='update'),
    path('delete/<int:pk>/', delete_idea, name='delete'),











    # path('base/', base, name='base'),
    
    # path('ideas/list/', ideas.IdeaListView. as_view(), name='list'),
    # path('ideas/create/', ideas.IdeaCreateView.as_view(), name='create'),
    # path('ideas/<int:pk>/update/', ideas.IdeaUpdateView.as_view(), name='update'),
    # path('ideas/<int:pk>/delete/', ideas.IdeaDeleteView.as_view(), name='delete'),
    # path('ideas/<int:pk>/detail', ideas.IdeaDetailView.as_view(), name='detail'),
]
