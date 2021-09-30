from django.urls import path
from . import views


urlpatterns = [
    path('product/chats/',views.view_chats_for_products,name='viewchats'),
    path('<str:product_name>/',views.index,name='chat'),
    path('<str:product_name>/<str:consumer_name>/',views.owner_chat,name='owner_chat'),
    path('send/msg/<int:id>/',views.send_msg,name='send'),
    path('owner/send/msg/',views.owner_msg,name='Omsg'),
    path('view/msgs/<str:pro>/',views.view_all_msgs,name='Vmsgs'),
    path('del/asker/<int:user_id>/',views.del_asker,name='delAsker'),
    path('view/unseen/msgs/',views.view_unseen_msgs,name='unseen'),
]