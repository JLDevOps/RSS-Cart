# RSS-Cart
Flask app that hosts an RSS feed that is generated from multiple RSS feeds.

## Add RSS Feeds and Merge Them
You can add multiple RSS feeds for the app to mix and merge them into your own unique RSS feed.

Go to the "settings.ini" file in the "app" folder, and update the "FEEDLIST" variable with your own RSS links.

## Setup App
### Running on a Linux Server
You can deploy this application on the server by doing the following:
1. Install the Python Packages
    ```
    pip install -r requirements.txt
    ```
2. Run the wsgi.py file
    ```
    python wsgi.py
    ```
3.  You should see it deployed on localhost.

### Running on a Heroku
You can deploy this application on Heroku by forking this template onto your own repo, and updating the "settings.ini" file with your own information

Go to the Heroku dashboard - https://dashboard.heroku.com/