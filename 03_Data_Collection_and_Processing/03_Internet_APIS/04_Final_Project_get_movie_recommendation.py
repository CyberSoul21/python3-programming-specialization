
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
import requests
import requests_with_caching
import json


def get_movies_from_tastedive(movie_str):
    parameters = {"q": movie_str, "type": "movies", "limit": 5}
    tastedive_response = requests_with_caching.get("https://tastedive.com/api/similar", params=parameters)
    result_data = json.loads(tastedive_response.text)
    return result_data

def extract_movie_titles(data):
    mv_names = []
    mv_inf = data['Similar']['Results']
    for name in mv_inf:
        mv_names.append(name['Name'])
    return mv_names  


def get_related_titles(list_movie):
    print(list_movie)
    lst = list()
    for title in list_movie:
        mv = get_movies_from_tastedive(title)
        til = extract_movie_titles(mv)
        for movie in til:
            if movie not in lst:
                lst.append(movie)
    return lst


def get_movie_data(mv_name):
    base_url= "http://www.omdbapi.com/"
    param = {}
    param["t"]= mv_name
    param["r"]= "json"
    result = requests_with_caching.get(base_url, params=param)
    print(result.url)
    result_j = result.json()
    return result_j

def get_movie_rating(mov_dict):
    l = len(mov_dict['Ratings'])
    rotten_rating = 0
    l_r = 0
    print(l)
    v=""
    rotten_rating = []
    for x in mov_dict['Ratings']:
        if x['Source'] == 'Rotten Tomatoes':
            print(x['Value'])
            l_r = len(x['Value'])    
            v = x['Value']
            
    if v != "":
        rotten_rating = int(v[0:l_r-1])
    else: rotten_rating = 0
    return rotten_rating


def get_sorted_recommendations(lst_mv_til):
    lst_mv= get_related_titles(lst_mv_til)
    lst_mv= sorted(lst_mv, key = lambda mv_name: (get_movie_rating(get_movie_data(mv_name)), mv_name), reverse=True)
    
    return lst_mv
