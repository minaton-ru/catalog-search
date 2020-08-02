from django.contrib import admin
from django.urls import path
from catalog import views
from catalog.views import index_search 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_search, name='search_results'),
]
