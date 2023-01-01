import requests
import wikipedia
import json

# let's start with nothing
nothing = '' # this isn't anything.

# so we want to find something that is something (not nothing) from wikipedia.

# we can use the wikipedia api to find something that is something (not nothing)
# https://en.wikipedia.org/wiki/Special:RandomInCategory/Random_page_in_category
random_page = wikipedia.random(pages=1) # this is something (not nothing)
