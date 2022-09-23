from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_index, name='menu_index'),               #トップページ表示用
    path('create', views.create, name='create'),                 #オブジェクト作成用
    path('edit/<int:num>', views.edit, name='edit'),             #編集用
    path('delete/<int:num>', views.delete, name='delete'),       #削除用
    path('find', views.find, name='find'),                       #検索用
    path('<int:num>', views.menu_index, name='menu_index'),      #ページネーション用
    path('favorite/<int:num>', views.favorite, name='favorite'), #お気に入り登録/解除用
]