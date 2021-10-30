from django.urls import path

from .views import (
    account_view
)

app_name='accounts' # recipes:list
urlpatterns = [
    path("", account_view, name='list'),
    #path("create/", recipe_create_view, name='create'),
    #path("<int:id>/edit/", recipe_update_view, name='update'),
    #path("<int:id>/", recipe_detail_view, name='detail'),
]