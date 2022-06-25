import requests
import json
import pandas as pd
from os.path import exists
import idresearch
# Tests by checking known reccomended papers with csv file results

url = 'https://arxiv.org/abs/2106.10353'


df = idresearch.get_reco_df(url)
df.to_csv(r'file1.csv')
if exists(r'file1.csv') == 1:
    print('Test Passed')
else:
    print('Test Failed')