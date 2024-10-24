from django.urls import path
from .views import *
urlpatterns = [
    path('serializer/',ProductsView.as_view()),
    path('serializer/<int:id>/',ProductsViewById.as_view()),

]
