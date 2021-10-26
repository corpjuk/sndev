from django.urls import path

from .views import (

    #put views here
    question_list_view,
    question_detail_view,
    add_question_view,
    # recipe_list_view,
    # recipe_detail_view,
    # recipe_create_view,
    # recipe_update_view
)

app_name='CNA' # recipes:list
urlpatterns = [
    path("", question_list_view, name='list'),
    # path("create/", recipe_create_view, name='create'),
    # path("<int:id>/edit/", recipe_update_view, name='update'),
    path("<int:id>/", question_detail_view, name='detail'),
    path('addQuestion/', add_question_view,name='addQuestion')
    # path("", recipe_list_view, name='list'),
    # path("create/", recipe_create_view, name='create'),
    # path("<int:id>/edit/", recipe_update_view, name='update'),
    # path("<int:id>/", recipe_detail_view, name='detail'),
]