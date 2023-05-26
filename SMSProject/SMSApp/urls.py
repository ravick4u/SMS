from django.urls import path
from .views import StudentListView

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('students/', StudentListView.as_view(), name='student-list'),
]