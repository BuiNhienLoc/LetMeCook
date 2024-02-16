from django.urls import path
from .views import menu_items, single_item, secret, manager_view,throttle_check,throttle_check_auth,managers

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', menu_items, name='menu-items-list'),
    path('menu-items/<int:pk>', single_item, name='single-item-view'),
    path('secret/',secret),
    path('api-token-auth/',obtain_auth_token),
    path('manager-view/', manager_view),
    path('throttle-check', throttle_check),
    path('throttle-check-auth',throttle_check_auth),
    path('groups/manager/users', managers),
]