from django.urls import path
from rooms import views as room_views

app_name = 'core'

urlpatterns = [path('', room_views.HomeView.as_view(), name='home')
               ]  # path('') 은 /을 의미(home)
                #path는 오로지 url과 함수만 갖는다. 따라서 HomeView(class)만 쓰면 안되고, 그 안의 함수를 넣어야 한다
