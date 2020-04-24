from django.urls import path,include
from . import views
urlpatterns = [
    path('<int:post_id>/',views.PostView.as_view(),name='post_view'),
    path('list/<int:page>/',views.PostListView.as_view(),name='post_list_view'),
    path('category/',views.CategoryView.as_view(),name='category_view'),
    path('category/<str:name>/<int:page>/',views.CategoryListView.as_view(), name='categorylist_view')
]