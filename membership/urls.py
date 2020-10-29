from django.urls import path
from membership import views

app_name = "membership"

urlpatterns = [
    path('<int:user_n>/information/', views.information, name="information"),
    path("<int:user_n>/information/recharge/", views.recharge, name="recharge"),
    path('<int:user_n>/information/history/', views.history, name="history"),
    path('<int:history_id>/information/history/create/', views.r_create, name="create"),
]
