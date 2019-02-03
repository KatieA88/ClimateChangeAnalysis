# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

#Get the libraries
import requests
import pandas as pd
import json
import os
import csv

#Set API and subscription details
url = 'http://api.planetos.com/v1/search/text?q=temperature&apikey=' + os.environ.get("API_KEY")

# Get Data
resp = requests.get(url).json()

climate = pd.DataFrame.from_dict(resp)
print (climate)

#climate.to_csv('climate.csv', sep = ',', encoding = 'utf-8')