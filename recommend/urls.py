# recommend/urls.py
from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
    # 访问 /recommend/quiz/ 时调用 quiz_view
    path('quiz/',views.quiz_view,   name='quiz'),
    # 访问 /recommend/result/ 时调用 result_view
    path('result/', views.result_view, name='result'),
]
