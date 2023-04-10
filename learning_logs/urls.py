"""Defines URL patterns for the APP learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Main page
    path('', views.index, name='index'),
    #Page that shows all the topics
    path('topics/', views.topics, name='topics'),
    #Page that shows the selected topic with its content
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding the new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for adding new entry (note) for the topic
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    #Page for editing existing entries (notes) for the topic
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]