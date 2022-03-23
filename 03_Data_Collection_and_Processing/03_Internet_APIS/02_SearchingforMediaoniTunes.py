import requests
#import requests_with_caching
import json

# You can explore the official iTunes API documentation.
#https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

#If we’re looking for podcasts originating in Ann Arbor, what value should be associated with the key “term”?
#params = {"term": "Ann Arbor"}


#Look at the iTunes API documentation. What is the key we need to use to only search for podcasts?

#params = {"media": "podcast"}


parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters,permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)


#import requests_with_caching
#import json

#parameters = {"term": "Ann Arbor", "entity": "podcast"}
#iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

#py_data = json.loads(iTunes_response.text)
#for r in py_data['results']:
#    print(r['trackName'])