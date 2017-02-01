======
 Tech Crunch dataset 
======

Overview
========

Data set from  Tech Crunch site. This Data Set created only for education purpose.

Data Set consist of next fields:
```
{"time": "2017-01-20 08:00:39", "tag": null, "author": "Khaled \"Tito\" Hamze", "title": "Crunch Report | Apple Suing Qualcomm for $1\u00a0Billion"},
```

For crawlin was used Scrapy. For more information including a list of features check the Scrapy homepage at: http://scrapy.org

For work with data set was created  jupyter notebook https://github.com/andriipetruk/techcrunch_dataset/blob/master/news_analytics.ipynb


Usage
============

#### Data set in json format 

https://raw.githubusercontent.com/andriipetruk/techcrunch_dataset/master/news.json


#### How to deploy and run spyder for get fresh data set
```
1. git clone git@github.com:andriipetruk/techcrunch_dataset.git
2. cd techcrunch_dataset
3. ./data_mining.sh
```

#### How to run notebook
```
1. cd techcrunch_dataset (if you are not there already)
2. jupyter notebook
3. go to the jupyter web UI and  open news_analytics.ipynb 
```

