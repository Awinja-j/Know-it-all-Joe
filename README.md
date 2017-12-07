# News_Aggregator

#### News Aggregator API is a structured service that provides access to information on the following categories

- Technology
- Finance
- Environment
- Sports
- Entertainment
- Politics

The API provides a simple wrapper around data being made available through the Scrappers

Data Sources:
Data is scrapped from the following websites:
##### Technology
1. https://techcrunch.com/
2. https://thenextweb.com/
3. https://www.wired.com/
##### Finance
1. https://finance.yahoo.com/
2. https://www.msn.com/
3. http://money.cnn.com/
##### Environment
1. https://www.treehugger.com/
2. http://www.realclimate.org/
3. http://grist.org/
##### Sports
1. http://www.espn.com/
2. https://sports.yahoo.com/
3. http://www.goal.com/en-ke/
##### Entertainment
1. https://www.hollywoodreporter.com/
2. http://www.tmz.com/
3. https://www.popsugar.com/
##### Politics
1. https://www.huffingtonpost.com/
2. https://www.washingtontimes.com/
3. http://thehill.com/

### Usage
###### Specification for the API are:


| URL Endpoint   | HTTP Method | Functionality     | Parameter |
|----------------|-------------|-------------------|-----------|
| /na/search/    | GET         | Search Query      | q=[query] |
| /na/[category] | GET         | Category          |           |
| /na/           | GET         | Displays all data |           |


### Development

Clone the repo from github `$ git clone https://github.com/Awinja-Andela/News_Aggregator.git`

Change directory into package `$ cd News_Aggregator`

Install the dependencies by running `$ pip install -r requirements.txt`

Run the server by running `$ python healthtools\manage.py runserver`

### Test



