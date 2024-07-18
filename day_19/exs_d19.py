# Day 19: 30 Days of python programming

# Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text.
#  All the files are in the data the folder:
   # a) Read "obama_speech.txt" file and count number of lines and words
   # b) Read "michelle_obama_speech.txt" file and count number of lines and words
   # c) Read "donald_speech.txt" file and count number of lines and words
   # d) Read "melina_trump_speech.txt" file and count number of lines and words
import os

def count_lines_words(file_path):
    if not os.path.exists(file_path):
        return "The provided file path does not exist, please check!"
    else:
        with open(file = file_path, mode = "r") as f:
            txt = f.readlines()
            n_line = len(txt)
            n_words = []
            for row in txt:
                n_words.append(len(row.split()))
            total_words = sum(n_words)
        return f"'{os.path.basename(file_path)}' has {n_line} lines and {total_words} words."

count_lines_words("./data/obama_speech.txt")
# "'obama_speech.txt' has 66 lines and 2400 words."
count_lines_words("./data/michelle_obama_speech.txt")
# "'michelle_obama_speech.txt' has 83 lines and 2204 words."
count_lines_words("./data/donald_speech.txt")
# "'donald_speech.txt' has 48 lines and 1259 words."
count_lines_words("./data/melina_trump_speech.txt")
# "'melina_trump_speech.txt' has 33 lines and 1375 words."


# 2. Read the "countries_data.json" data file in data directory,
#  create a function that finds the ten most spoken languages

#```py
## Your output should look like this
#print(most_spoken_languages(filename='./data/countries_data.json', 10))
#[(91, 'English'),
#(45, 'French'),
#(25, 'Arabic'),
#(24, 'Spanish'),
#(9, 'Russian'),
#(9, 'Portuguese'),
#(8, 'Dutch'),
#(7, 'German'),
#(5, 'Chinese'),
#(4, 'Swahili'),
#(4, 'Serbian')]
#
## Your output should look like this
#print(most_spoken_languages(filename='./data/countries_data.json', 3))
#[(91, 'English'),
#(45, 'French'),
#(25, 'Arabic')]
#```

import os
import json
def most_spoken_languages(filename, n_most):
    # open json data
    with open(file = filename, mode = "r") as file:
        countries_data = json.load(file)
        # init count
        lang_dict = {}
        # for each country, get the languages
        for country in countries_data:
            languages = country.get("languages", 0)
            # count for each language
            for i in languages:
                if i in lang_dict:
                    lang_dict[i] += 1
                else:
                    lang_dict[i] = 1
        # sort counts
        lang_dict_sorted = sorted(
            lang_dict.items(), key = lambda x: x[1], reverse = True)
        return lang_dict_sorted[:n_most]
    
most_spoken_languages(
    filename = "./data/countries_data.json",
    n_most = 10
)
most_spoken_languages(
    filename = "./data/countries_data.json",
    n_most = 3
)


# 3. Read the countries_data.json data file in data directory,
#  create a function that creates a list of the ten most populated countries

#```py
## Your output should look like this
#print(most_populated_countries(filename='./data/countries_data.json', 10))
#
#[
#{'country': 'China', 'population': 1377422166},
#{'country': 'India', 'population': 1295210000},
#{'country': 'United States of America', 'population': 323947000},
#{'country': 'Indonesia', 'population': 258705000},
#{'country': 'Brazil', 'population': 206135893},
#{'country': 'Pakistan', 'population': 194125062},
#{'country': 'Nigeria', 'population': 186988000},
#{'country': 'Bangladesh', 'population': 161006790},
#{'country': 'Russian Federation', 'population': 146599183},
#{'country': 'Japan', 'population': 126960000}
#]
#
## Your output should look like this
#
#print(most_populated_countries(filename='./data/countries_data.json', 3))
#[
#{'country': 'China', 'population': 1377422166},
#{'country': 'India', 'population': 1295210000},
#{'country': 'United States of America', 'population': 323947000}
#]
#```

import os
import json
def most_populated_countries(filename, n_most):
    # open json data
    with open(file = filename, mode = "r") as file:
        countries_data = json.load(file)
        # extract the two key-value pairs
        extraction = [
            {key: country[key] for key in ["name", "population"]}
            for country in countries_data
        ]
        # order by population
        sorted_extraction = sorted(extraction, key = lambda x: x["population"], reverse = True)
        return sorted_extraction[:n_most]

most_populated_countries(
    filename = './data/countries_data.json', n_most = 10)
most_populated_countries(
    filename = './data/countries_data.json', n_most = 3)


# Exercises: Level 2

# 1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
email_file = "./data/email_exchanges_big.txt"
with open(email_file) as file:
    txt = file.readlines() # read text line by line and store in a list of strings
email_pattern = r"\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]+\b" # regex pattern
unique_emails = { # use set comprehension to store unique values
    email
    for item in txt # iterate over each string (outer loop)
    if item.startswith("From ") # check condition
    for email in re.findall(email_pattern, item) # find email in each string (inner loop)
}


# 2. Find the most common words in the English language.
#  Call the name of your function find_most_common_words,
#  it will take two parameters -
#  a string or a file and a positive integer, indicating the number of words.
#  Your function will return an array of tuples in descending order.
#  Check the output

#```py
#    # Your output should look like this
#    print(find_most_common_words('sample.txt', 10))
#    [(10, 'the'),
#    (8, 'be'),
#    (6, 'to'),
#    (6, 'of'),
#    (5, 'and'),
#    (4, 'a'),
#    (4, 'in'),
#    (3, 'that'),
#    (2, 'have'),
#    (2, 'I')]
#
#    # Your output should look like this
#    print(find_most_common_words('sample.txt', 5))
#
#    [(10, 'the'),
#    (8, 'be'),
#    (6, 'to'),
#    (6, 'of'),
#    (5, 'and')]
#```

## didn't find sample.txt, use the speech txt
import re
def find_most_common_words(filename, n_most):
    # read all text together
    with open(filename) as file:
        txt = file.read()
        # split into words
        all_words = re.findall(r'\b\w+\b', txt) # find all word boudaries
        # get unique words
        unique_word = set(all_words)
        # count occurrence
        count_word = [(all_words.count(word), word) for word in unique_word]
        # sort counts
        count_sorted = sorted(count_word, key = lambda x: x[0], reverse = True)
        
        return count_sorted[:n_most]

find_most_common_words('./data/obama_speech.txt', 10)
find_most_common_words('./data/obama_speech.txt', 5)


# 3. Use the function, find_most_frequent_words to find:
   # a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
find_most_common_words('./data/obama_speech.txt', 10)
   # b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
find_most_common_words('./data/michelle_obama_speech.txt', 10)
   # c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
find_most_common_words('./data/donald_speech.txt', 10)
   # d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
find_most_common_words('./data/melina_trump_speech.txt', 10)


# 4. Write a python application that checks similarity between two texts.
#  It takes a file or a string as a parameter and
#  it will evaluate the similarity of the two texts.
#  For instance check the similarity between the transcripts of
#  [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#  and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech.
#  You may need a couple of functions, function to clean the text(clean_text),
#  function to remove support words(remove_support_words) and
#  finally to check the similarity(check_text_similarity).
#  List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory

## read texts
with open("./data/michelle_obama_speech.txt") as file:
    michelle_text = file.read()
with open("./data/melina_trump_speech.txt") as file:
    melina_text = file.read()

## clean text
import re
def clean_text(string):
    string = string.lower()
    return re.sub(pattern = "[^a-zA-Z\s]|[\\n]+", repl = "", string = string) 

michelle_clean = clean_text(michelle_text)
melina_clean = clean_text(melina_text)

## remove stop words
from stop_words import stop_words

def remove_stopword(text):
    words = text.split()
    clean_words = [word for word in words if word not in stop_words]
    return " ".join(clean_words)

michelle_clean_text = clean_text(michelle_clean)
melina_clean_text = clean_text(melina_clean)

## check similarity
# ??


# 5. Find the 10 most repeated words in the "romeo_and_juliet.txt"
find_most_common_words('./data/romeo_and_juliet.txt', 10)


# 6. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
   # a) Count the number of lines containing python or Python
   # b) Count the number lines containing JavaScript, javascript or Javascript
   # c) Count the number lines containing Java and not JavaScript
filepath = "./data/hacker_news.csv"
import csv

count_python_lines = 0
count_javascript_lines = 0
count_java_lines = 0
with open(file=filepath) as file:
    data = csv.reader(file, delimiter=",")
    for row in data:
        # check if the word 'python' (converted to lowercase) is in any field of the row
        if any('python' in field.lower() for field in row):
            count_python_lines += 1
        if any('javascript' in field.lower() for field in row):
            count_javascript_lines += 1
        if any('Java' in field for field in row) and not any('JavaScript' in field for field in row):
            count_java_lines += 1
print("Number of lines containing 'python' or 'Python':", count_python_lines)
print("Number of lines containing 'JavaScript', 'javascript' or 'Javascript':", count_javascript_lines)
print("Number of lines containing 'Java' and not 'JavaScript':", count_java_lines)