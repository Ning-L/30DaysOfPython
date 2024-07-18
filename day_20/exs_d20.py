# Day 20: 30 Days of python programming

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
## url does not exist, use the one from github
url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/romeo_and_juliet.txt"

import requests
response = requests.get(url=url)
print(response) # <Response [200]>
text = response.text

import re
def find_most_common_words(txt, n_most):
    # split into words
    all_words = re.findall(r'\b\w+\b', txt) # find all word boudaries
    # get unique words
    unique_word = set(all_words)
    # count occurrence
    count_word = [(all_words.count(word), word) for word in unique_word]
    # sort counts
    count_sorted = sorted(count_word, key = lambda x: x[0], reverse = True)
    
    return count_sorted[:n_most]

find_most_common_words(txt = text, n_most = 10)
# [(768, 'the'), (655, 'I'), (566, 'to'), (562, 'and'), (487, 'of'), (462, 'a'), (342, 'in'), (338, 'is'), (321, 'you'), (310, 'my')]


# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
    # 2-1. the min, max, mean, median, standard deviation of cats' weight in metric units.
cats_api = 'https://api.thecatapi.com/v1/breeds'
import requests
import json
response = requests.get(url=cats_api)
print(response) # <Response [200]>
text = response.text # get the string of json data
cat_dict = json.loads(text) # convert the json to a list of dictionaries

# cat_dict is a list of dictionaries of dictionaries
# extract the metric of weight
metric_range = [cat_i.get("weight").get("metric") for cat_i in cat_dict] 
# extract numbers from the strings
weights = [int(i) for range in metric_range for i in range.split(" - ")]
# do stats
import numpy as np
np.min(weights)
np.max(weights)
np.median(weights)
np.mean(weights)
np.var(weights)

    # 2-2. the min, max, mean, median, standard deviation of cats' lifespan in years.
# same for the lifespan
lifespan_range = [cat_i.get("life_span") for cat_i in cat_dict] 
lifespan = [int(i) for j in lifespan_range for i in j.split(" - ")]
np.min(lifespan)
np.max(lifespan)
np.median(lifespan)
np.mean(lifespan)
np.var(lifespan)

    # 2-3. Create a frequency table of country and breed of cats
countries = [cat_i.get("country_code") for cat_i in cat_dict] 
country_count = [{i: countries.count(i)} for i in set(countries)]

breeds_link = [cat_i.get("cfa_url") for cat_i in cat_dict] 
import re
breeds = [re.search(r'(.*)\.aspx', i.split("/")[-1]).group(1) for i in breeds_link if i is not None]
## get the part of breed from the url of cfa, only do it when url is not None
breeds_count = [{i: i.count(i)} for i in breeds]


# 3. Read the countries API and find
country_api = "https://restcountries.eu/rest/v2/all"
    # 3-1. the 10 largest countries
    # 3-2. the 10 most spoken languages
    # 3-3. the total number of languages in the countries API
## link broken

# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
## link broken