# Billboard-Wiki

It scrapes song names and artists from billboard , the creates a valid Wikipedia link from that data for that particular song . The it extracts song writers and genres for all songs , creates a pandas dataframe and stores it as csv file

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python or PyCharm

### Installing

There are two ways you can run the program

1. Using PyCharm

         1.1 Just clone the project and Under new option in PyCharm , select this folder and you would be good to go .


2. Using Basic Python 
   
   2.1 Install Pandas as 

```
pip install pandas
```
   2.2 Install Requests

```
pip install Requests
```
   2.3  Install BeautifulSoup4

```
pip install beautifulsoup4
```
  
   2.4 Install html5lib
   
```
pip install html5lib
```


### Running the tests

1. First set Dates in data.py as to from which date to whic date you want the billboard data for .
2. Change the number by which i is divided .From this you can change intervals , as to once per 30 days if the number is 30
3. Run main.py and then it will generate a csv file name example .csv

