from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'programmers',views.ProgrammerViewSet)
router.register(r'tickets',views.TicketsViewSet)
router.register(r'orders',views.OrdersViewSet)
router.register(r'cliente',views.ClienteViewSet)

urlpatterns=[
    path('',include(router.urls))

]