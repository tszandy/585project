#!/usr/bin/python
from Turney import *

game_reviews=read_amazon_review('amazondataset/Video_Games_5.json')

print findword('yummy', game_reviews)