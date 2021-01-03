import feedparser
from feedgen.feed import FeedGenerator
import dateutil.parser
import configparser
import ast
import os
import time

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),'settings.ini'))
FEED_LIST = config.get("DEFAULT", "FEEDLIST")

def get_entry(n):
    return feedparser.parse(n)['entries']

def get_feed_list():
    feeds = map(get_entry,ast.literal_eval(FEED_LIST))
    feed = [item for feed in feeds for item in feed]
    feed.sort(key=lambda x: dateutil.parser.parse(x['published']), reverse=False)
    return feed

def create_rss_feed(filename='rss-new.xml'):
    fg = FeedGenerator()
    fg.id(config.get("DEFAULT", "WEBSITE"))
    fg.title(config.get("DEFAULT", "RSSTITLE"))
    fg.description(config.get("DEFAULT", "RSSDESCRIPTION"))
    
    fg.author
    ( 
        {
            "name": config.get("DEFAULT", "AUTHOR"),
            "email": config.get("DEFAULT", "EMAIL")
        } 
    )

    fg.link(href=config.get("DEFAULT", "RSSLINK"), rel='self' )
    fg.subtitle(config.get("DEFAULT", "RSSSUBTITLE"))
    fg.language(config.get("DEFAULT", "LANGUAGE"))
    feed = get_feed_list()

    for entry in feed:
        fe = fg.add_entry()
        fe.id (entry.id)
        fe.title(entry.title)
        fe.description(entry.description)
        fe.published(entry.published)
        fe.pubDate(entry.published)
        fe.link(href=entry.id)
    
    # Uncomment the bottom if you want an Atom RSS file created instead of an rss.xml
    # atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
    # fg.atom_file('atom-new.xml') # Write the ATOM feed to a file

    rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
    fg.rss_file(filename) # Write the RSS feed to a file
    return fg