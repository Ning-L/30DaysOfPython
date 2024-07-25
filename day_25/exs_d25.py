# Day 25: 30 Days of python programming

import numpy as np
import pandas as pd

# Read the hacker_news.csv file from data directory
df = pd.read_csv("data/hacker_news.csv")

# Get the first five rows
df.head(5)
        #  id  ...       created_at
# 0  12224879  ...   8/4/2016 11:52
# 1  11964716  ...  6/23/2016 22:20
# 2  11919867  ...   6/17/2016 0:01
# 3  10301696  ...   9/30/2015 4:12
# 4  10482257  ...  10/31/2015 9:48

# Get the last five rows
df.tail()

# Get the title column as pandas series
df.columns
titles = df["title"]
type(titles)

# Count the number of rows and columns
df.shape # (20099, 7)

# Filter the titles which contain python
title_lst = list(titles)
len(title_lst)
type(title_lst)
title_lst[0].find("python") # no match returns -1
python_title = [title for title in title_lst if title.find("python") != -1]
len(python_title) # 12
python_title

# Filter the titles which contain JavaScript
javascript_title = [title for title in title_lst if title.find("JavaScript") != -1]
len(javascript_title) # 169

# Explore the data and make sense of it
df.info()
df.describe(include="all")
df.describe()

### Notes: VScode cmd+opt+up/down to add new cursor up or down