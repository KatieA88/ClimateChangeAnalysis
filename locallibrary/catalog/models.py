# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

#Get the libraries
import requests
import pandas as pd
import json
import os

#Set API and subscription details
url = 'http://api.planetos.com/v1/search/text?q=temperature&apikey=' + os.environ.get("API_KEY")

# Get Data
resp = requests.get(url).json()

#Create a dataframe
df = pd.DataFrame.from_dict(resp, orient='index')
print (df)
