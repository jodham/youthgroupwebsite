from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', enter, name='login'),
    path('validate/', validate, name='validate'),
    path('logout/', getout, name="logout"),
    path('', IndexView.as_view(), name="index"),
    path('members/', MembersListView.as_view(), name="members"),
    path('member/<int:pk>/', MembersDetailView.as_view(), name="member_detail"),
    path('project/<int:pk>/', projectDetailView.as_view(), name='project_detail'),
    path('posts/', PostView.as_view(), name='posts'),
    path('post/new', postCreateView.as_view, name='post_view')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
