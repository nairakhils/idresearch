
from os.path import exists
import idresearch

url = 'https://arxiv.org/abs/2106.10353'

idresearch.export_reco_csv(url)
# exports csv to idresearch directory

if exists(r'recolist.csv')==1:
    print('Test Passed')
else:
    print('Test Failed')
