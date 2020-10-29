from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 로그인/로그아웃
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.log_out, name='logout'),
    # 고객의소리
    path('list/', views.p_list, name='list'),
    path('create_voc/', views.p_create, name='create_voc'),
    path('<int:post_id>/delete/', views.p_delete, name='delete'),
    path('<int:post_id>/update/', views.p_update, name='update'),
    path('<int:post_id>/detail/', views.p_detail, name='detail'),
    path('<int:comment_id>/<int:post_id>/c_delete/', views.c_delete, name='c_delete')
]
