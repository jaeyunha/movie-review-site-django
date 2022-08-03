from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '24f7c99927298a37d37cd8fd31b1bdfd'
def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_id+'&query='+searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
        # https://api.themoviedb.org/3/search/movie?
        # api_key=24f7c99927298a37d37cd8fd31b1bdfd&language=en-US&query=hello&page=1&include_adult=false
        # 위 형태의 url로 get 요청 보내기
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/all/day?api_key='+my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']

    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):

    url = 'https://api.themoviedb.org/3/movie/'+ movie_id + 'api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detial.html', {"redata": resdata})

    return