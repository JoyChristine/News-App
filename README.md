
## Description

News App is a web application that will help users list and preview news articles from various sources.
It is a web application that is meant to catch up hard workers on current affairs happening all over the world.

## Features
-The home page allows one to see highlights from different sources and also various news sources sorted based on categories and select their preference.
- Once a user selects a source, a list of all articles for that news source with image description and time of posting article is shown.
- User can click on an article and read it fully from the news source.
- Users can additionally click top headlines to see top headline articles.
- Users can also search for specific articles.


# Behavior Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View All News Sources | Default Home Page(right)| Displays all news sources |
|View Top Headlines | Default home page (left)| Displays Top Headlines articles |
| View Categories of news sources| Click on any category on teh navbar | Redirects to the specified category articles page|
| Search for an article by keyword | Type any keyword in `search bar` e.g. `Kenya`| Redirects to search page with all the search results for Kenya|

## View Live Site here
View the complete site [here](https://newsapp-joy.herokuapp.com/)


## Technologies Used
    - Python 3.8
    - Flask Framework
    - HTML, CSS and Bootstrap
 


## Set-up and Installation
    1. Clone or download the Repo
    2. Create a virtual environment i.e python3 -m venv <name-of-virtual-environment>
    3. Get the Api Key from the NewsAPI.org https://newsapi.org/
    4. Edit the start.sh file with your api key from the news.org website   
    6. Run chmod a+x start.py
    7. Run python3 manage.py runserver
    8. Access the application through `localhost:5000`

## Known bugs
No known bugs so far. If found drop me an email.

## Contributors
    - Joy Christine Nduta Kimani

### Contact Information
joychristin2@gmail.com
