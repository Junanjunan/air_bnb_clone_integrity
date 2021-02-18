"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from . import settings 로 하면 안됨
# setting를 import 하고 싶을 떄 위의 방식으로 해야 장고가 어떤 setting 파일들을 내가 가르키는지를 알게 될 것이고, 기본적으로 그것(내가 가리키는 것)은 settings에 가진 파일을 반영한 것을 말하고 있는 것임. 그래서 파일을 임포트 하는게 아니다(파일명은 바뀔수도 있기 때문에). 파일을 반영한 것을 import 함
from django.conf.urls.static import static
# static : 장고에서 static 파일들을 제공하는 걸 돕는 헬퍼.

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('rooms/', include('rooms.urls', namespace='rooms')),
    path('users/', include('users.urls', namespace='users')),
    path('reservations/', include('reservations.urls', namespace='reservations')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('lists/', include('lists.urls', namespace='lists')),
    path('admin/', admin.site.urls),
]

# 프로덕션모델인지, 개발모델인지 감지하기를 원할 떄 아래를 이용 (DEBUG=True는 개발 중을 의미하므로)
# 아래는 if는 개발모드가 참이라면을 의미
# 개발 모드에서만 나의 static 파일들이 사용되어지도록 하기 위한 것임 (static 파일이나 업로드 된 파일들을 내 서버에서 사용하지 않도록 - 서버 디스크 공간을 아끼기 위해)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# settings 에서 지정해준 /media/ 폴더를 제공하고 싶다고 static에게 말할거임
# url(/media/)을 폴더(MEDIA_ROOT) 에 연결시켜주기 위해서 static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)를 해줌
# 이는 라우터를 생성해 준 것임
