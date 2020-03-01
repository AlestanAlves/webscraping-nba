## Web Scraping NBA (with JS Dynamic)

- fix error in geckodriver

```
export GV=v0.26.0
wget "https://github.com/mozilla/geckodriver/releases/download/$GV/geckodriver-$GV-linux64.tar.gz"
tar xvzf geckodriver-$GV-linux64.tar.gz 
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/
```

- Requirements 

```
import time
import requests
import pandas as pd
import bs4 as BeatifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
``` 
