
from django.contrib import admin
from django.urls import path, include

##############################ini untuk menampilkan gambar yang sudah di upload pada folder media#####################################################
from django.conf import settings
from django.conf.urls.static import static

from myproject.views import home, about, contact, detail_artikel
from myproject.authentifikasi import akun_login, akun_logout, akun_registrasi

from berita.api import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dashboard/', include("berita.urls")),
    path('authentifikasi/login', akun_login, name="akun_login"),
    path('authentifikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentifikasi/logout', akun_logout, name="akun_logout"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/kategori/list', api_kategori_list),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),
    path('api/artikel/list', api_artikel_list),
    path('api/author/list', api_author_list),
    path('api/kategori/add', api_kategori_add),
    path('api/artikel/add', api_artikel_add),
]

##############################ini untuk menampilkan gambar yang sudah di upload pada folder media#####################################################
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)