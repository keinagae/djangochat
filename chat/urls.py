from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
    path('<int:room>/', views.room, name="room"),
    path('token', views.ChatTokenGeneratorApiView.as_view()),
    path('messages/<int:conversion>', views.MessageListAPIView.as_view()),
    path('contacts/',views.ChatNewContactApiView.as_view()),
    path('', views.ChatListCreateApiView.as_view())
]
