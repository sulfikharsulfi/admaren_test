from django.urls import path
from .views import RegisterView,LoginView,OverviewAPI,CreateAPI,TagCreateAPIView,DetailAPI,UpdateAPI,DeleteAPI,TagListAPI,TagDetailAPI


urlpatterns = [
    path('register/',RegisterView.as_view(),name='register_view'),
    path('login/',LoginView.as_view(),name = 'login_view'),
    path('snippet/list',OverviewAPI.as_view(),name = 'over_api_view'),
    path('snippet/create/',CreateAPI.as_view(),name = 'create_api_view'),
    path('tag/create/',TagCreateAPIView.as_view(),name = 'tag_list_create'),
    path('snippet/<int:pk>',DetailAPI.as_view(),name = 'snippet_detail_view'),
    path('snippet/update/<int:pk>/',UpdateAPI.as_view(),name = 'update_api_view'),
    path('snippet/delete/<int:pk>/',DeleteAPI.as_view(),name = 'delete_api_view'),
    path('tag/list/',TagListAPI.as_view(),name = 'tag_list_view'),
    path('tag/<int:pk>',TagDetailAPI.as_view(),name = 'tag_detail_api_view')
]   