from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('subtopic/<int:subtopic_id>/', views.subtopic_detail, name='subtopic_detail'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('practice/', views.practice_problems, name='practice_problems'),
    
    # API endpoints
    path('api/topics/', views.api_topics, name='api_topics'),
    path('api/topic/<int:topic_id>/', views.api_topic_detail, name='api_topic_detail'),
    path('api/problem/<int:problem_id>/', views.api_problem_detail, name='api_problem_detail'),
    path('api/submit/', views.api_submit_code, name='api_submit_code'),
]
