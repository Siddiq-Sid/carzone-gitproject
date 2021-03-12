from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    featured_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(featured_cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('car_model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct

    data = {
        'featured_cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request,'cars/cars.html', data)

def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {
        'car': car
    }
    return render(request, 'cars/car_details.html', data)

def search(request):

    model_search = Car.objects.values_list('car_model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct

    search_cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars = search_cars.filter(car_title__icontains = keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            search_cars = search_cars.filter(car_model__iexact = model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            search_cars = search_cars.filter(city__iexact = city)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            search_cars = search_cars.filter(body_style__iexact = body_style)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            search_cars = search_cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'search_cars':search_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request,'cars/search.html',data)