
import idresearch
"""

Tests by giving known paper url and checking for paper-id match

"""

url = 'https://arxiv.org/abs/2106.10353'
paper_id = 'd9c5081c542e91d09784b27a793356124715edfe'

a,b,c =idresearch.get_doc(url)

if b == paper_id:
    print('Test Passed')
else:
    print('Test Failed')


