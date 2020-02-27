import time
import requests
import pandas as pd
import bs4 as BeatifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"