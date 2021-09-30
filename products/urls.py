from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path("view/<int:number>/",views.view_product, name="vpro"),
    path('add',views.add_product,name='add'),
    path('delete/<int:pk>/',views.del_product,name='delPro'),
    path('edit/<int:pk>/',views.edit_product,name='editPro'),
    path('save/<int:id>/',views.save_prod,name='saved'),
    path('view/saved/',views.view_saved,name='Vsaved'),
]