from django.urls import path, include
from . import views
from .views import StudentApiView,StudentDetailApi,StudentGenericView,StudentViewset

#Routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', StudentViewset, basename='student')

urlpatterns = [
    
    path('',views.student_list, name = 'students'),
    path('function/<int:pk>/',views.details, name = 'detail'),

    # path('',StudentApiView.as_view()),
    # path('class/<int:pk>/',StudentDetailApi.as_view()),

    # path('',StudentApiView.as_view()),
    # path('generic/<int:pk>/',StudentGenericView.as_view())

    # path('', include(router.urls)),
    # path('<int:pk>/', include(router.urls)),
    


]

# first and second paths applies to functional based views
# second are third are for class based
# fourth and fifth applies to generic
# sixth and seventh applies to viewsets