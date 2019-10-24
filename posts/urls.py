from django.urls import path
from . import views
urlpatterns=[

path('addpost/<int:user_id>',views.add_post,name='addpost'),
path('postdetail/<int:id>',views.post_detail,name='postdetail'),
path('postedit/<int:id>/<int:user_id>',views.post_edit,name='postedit'),


]