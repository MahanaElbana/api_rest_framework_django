
from django.urls import path ,include
from django.urls.resolvers import URLPattern
from api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('ModelViewSet',views.viewset_list_pk, basename='ModelViewSet')
router.register('ViewSet',views.GeustViewSet, basename='ViewSet')
router.register('TheLast',views.TheLastViewSet, basename='thelast')

urlpatterns = [
  path('method1/',views.get_static_data_no_rest_no_model),

  path('method2/',views.get_data_no_rest_from_model),

  path('method3-1/',views.fbv_list),
  path('method3-2/<int:pk>/',views.fbv),

   path('method4-1/',views.CBV_LIST.as_view()),
   path('method4-2/<int:pk>/',views.CBV.as_view()),

   path('method5-1/',views.Mixin_list.as_view()),
   path('method5-2/<int:pk>',views.Mixin_pk.as_view()),

   path('method6-1/',views.generics_list.as_view()),
   path('method6-2/<int:pk>/',views.generics_pk.as_view()),

   path('method7-8/',include(router.urls)),

   ## trial code := 
   path('trialcode/',views.TrialCode.as_view())
]