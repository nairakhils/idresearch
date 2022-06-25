import idresearch

url ='https://arxiv.org/abs/2106.10353'

s=[]

s= idresearch.reco_authors(url,5)

if s==[]:
    print('Test Failed')
else:
    print("Test Passed")