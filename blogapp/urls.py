from django.urls import path  
from .views import PostList, PostDetail, CategoryList, CategoryDetail

app_name = 'blogapp'  
urlpatterns = [  
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),  
    path('categories', CategoryList.as_view(), name='category-list'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
]