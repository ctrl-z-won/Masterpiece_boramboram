from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import Mainscreen.views
import servicecenter.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainscreen.views.home, name='home'),
    path('servicecenter/', servicecenter.views.home, name='servicecenter'),
    path('servicecenter/<int:servicecenter_id>/', servicecenter.views.detail, name='detail'),
    path('servicecenter/write/', servicecenter.views.write, name='write'),
    path('servicecenter/create/', servicecenter.views.create, name='create'),
    path('accounts/', include('accounts.urls')),
]
