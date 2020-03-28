from api.views import product_list, product_details, categories_list, category_details, products_by_cat_id
from django.urls import path
urlpatterns = {
    path('products/',product_list),
    path('products/<int:id>/',product_details),
    path('categories/',categories_list),
    path('categories/<int:id>/',category_details),
    path('categories/<int:id>/products/',products_by_cat_id)
}