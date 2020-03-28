from django.shortcuts import render
import json
from django.http.response import HttpResponse, JsonResponse
products = []
# for i in range(1, 10):
#     products.append(
#     {
#         'id': i,
#         'name': f'Product {i}',
#         'price': 2000.45 +i*i*i*i,
#         'decription': f'Product {i} is good!',
#         'count': 45+i*i
#     })
products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': 2000.45 +i*i*i*i,
        'decription': f'Product {i} is good!',
        'count': 45+i*i
    } for i in range(1, 20)
]
categories = [
    {
        'id': i,
        'name': f'Categories {i}',
    } for i in range(10,12)
]
def categories_list(request):
    return JsonResponse(categories)

def product_list(request):
    return JsonResponse(products, safe = False)

def category_details():
    for cat in categories:
        if cat['id'] == id:
            return JsonResponse(cat)
        return JsonResponse({'error': 'This page not found'})

def product_details(request, id):
    for prod in products:
        if prod['id'] == id:
            return JsonResponse(prod)
        return JsonResponse({'error': 'This page not found'})

def products_by_cat_id(request, id, products):
    for prod in products:
        if len(prod['id']) == id[0]:
            return JsonResponse(prod)
    return JsonResponse({'error': 'This page not found'})